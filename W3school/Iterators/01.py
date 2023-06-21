
import random as rnd


size = 200
n = 4
m_r= 0.8


def init_population(size , n):
    list = []
    for i in range(size):
        member = []
        for j in range(n) :
            member.append(rnd.randint(1,n))
        member.append(0)
        list.append(new_member)
    
    return list

def diff(list):
    for i in range(0,len(list),2):
        child1 = list[i][:len(population[0])//2] + 
list[i+1][len(population[0])//2 : len(population[0])-1]
        child2 = list[i+1][:len(population[0])//2] + list[i][len(population[0])//2 : len(population[0])-1]
        child1.append(0)
        child2.append(0)
        list.append(child1)
        list.append(child2)
        
    return list

def mutaion(list , mutation_rate , n):
    choosen_ones = [i for i in range(len(list)//2 , len(list))]
    for i in range(len(list)//2):   
        new_random = rnd.randint(0 , len(list)//2 -1)
        choosen_ones[new_random] , choosen_ones[i] = choosen_ones[i] , choosen_ones[new_random]
    choosen_ones = choosen_ones[:int(len(choosen_ones)* mutation_rate)]
    for i in choosen_ones:
        new_ch = rnd.randint(0 , n-1)
        new_value = rnd.randint(1,n)
        list[i][new_ch] = new_value
        
    return list

def Evalution(list , n):
    for v in list:
        Conflicte = 0
        for i in range(n):
            for j in range(i+1,n):
                
                if(v[i] == v[j]):
                    Conflicte += 1
                if(abs(v[i] - v[j]) == abs(j - i)):
                    Conflicte += 1
                    
        v[len(v) - 1] = Conflicte
    list.sort(key = lambda x: x[n])    
    return list

population = init_population(size , n)
population = Evalution(population , n)
if(population[0][n] == 0):
        print(f"PP solve problem : {population[0]}")
else:
    
    for i in range(int(population_size / 2)):
        population = cross_over(population)
        population = mutaion(population , m_r , n)
        population = Evalution(population , n)
        population = population[:len(population)//2]
        if(population[0][n] == 0):
            print(f"solve problem in Community {i} : {population[0][0:n]}")
            break
    
