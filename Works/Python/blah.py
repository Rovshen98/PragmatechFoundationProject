# Hər hansı bir natural n ədədini götürək.
#  Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək.
#  Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və 
# sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır.
n=(int(input()))
list=[]
list.append(str(n))

for x in list:
    print()
    x+1