#!/bin/bash
get_cpu_times(){
    read -r cpu user nice system idle iowait irq softirq steal guest guest_nice < /proc/stat
    total_times=$(($user + $nice + $system + $idle + $iowait + $irq + $softirq + $steal + $guest + $guest_nice))
    echo "$idle $total_times"
}

get_memory_usage(){
    mem_total=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    mem_available=$(grep MemAvailable /proc/meminfo | awk '{print $2}')
    mem_free=$(grep MemFree /proc/meminfo | awk '{print $2}')
    mem_used=$((mem_total - mem_available))
    mem_usage_percentage=$(echo "scale=2; 100 * $mem_used / $mem_total" | bc)
    mem_free_percent=$(echo "scale=2; 100 * $mem_free / $mem_total" | bc)
    echo "$mem_free $mem_used $mem_usage_percentage $mem_free_percent"
}

get_disk_usage(){
    read -r total used free percent < <(df -h --output=size,used,avail,pcent "/" | tail -1)
    echo "$total $used $free $percent"
}

get_top_five_processes(){
    ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
}

get_top_five_processes_by_memory(){
    ps -eo pid,comm,%mem --sort=-%mem | head -n 6
}

# calculating the CPU usage
read -r idle1 total1 < <(get_cpu_times)
sleep 1
read -r idle2 total2 < <(get_cpu_times)
idle_diff=$((idle2 - idle1))
total_diff=$((total2 - total1))
usage=$(echo "scale=2; 100 * ($total_diff - $idle_diff) / $total_diff" | bc)

# calculating the memory usage
read -r mem_free mem_used mem_usage_percentage mem_free_percent < <(get_memory_usage)

# calculating the disk usage
read -r disk_total disk_used disk_free disk_percent < <(get_disk_usage)

# showing all the stats
echo "Uso total da CPU: $usage%" 
echo "Uso total da memória : $mem_usage_percentage% / Memória livre : $mem_free kb / Memória usada : $mem_used kb"
echo "Memória livre: $mem_free_percent%"
echo "Uso total do disco: $disk_percent / Total: $disk_total / Usado: $disk_used / Livre: $disk_free"
echo "Top 5 processos por uso de CPU:"
get_top_five_processes
echo "Top 5 processos por uso de memória:"
get_top_five_processes_by_memory
