cat */A_to_I.res > ALL_A_to_I.res
bedtools sort -i ALL_A_to_I.res > ALL_A_to_I.res.sorted
cut -f 1,2,3,4 ALL_A_to_I.res.sorted | uniq > ALL_A_to_I.res.sorted.uniq.bed
