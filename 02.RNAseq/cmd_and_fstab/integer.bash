A=3
B=2
echo "====== method 1 ======="
let C=$A+$B
echo "'C=$A+$B', C is $C"
echo "====== method 2 ======="
D=$[$A+$B]
echo "'D=$[$A+$B]', D is $D"
echo "====== method 3 ======="
E=$(($A+$B))
echo "'E=$(($A+$B))', E is $E"
echo "====== method 4 ======="
F=`expr $A+$B`
echo "'F=expr $A+$B', F is $F"



