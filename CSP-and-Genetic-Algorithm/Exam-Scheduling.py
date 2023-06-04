                                                  #ASSIGNMENT # 2
                                                    #Dania Jawad
                                                     #20i-0569
                                                       #CS-B

import random
import time
import numpy as np

courses = ["C1","C2","C3","C4","C5"] #list of courses
halls = ["H1","H2"] #list of halls
hallTiming = ["3" , "6"] #list of hall timings
timeAvail = ["T1","T2","T3"] #list of time slots

conflicts = [("C1","C2"),("C1","C4"),("C2","C5"),("C3","C4"),("C4","C5")] #list of tuples of conflicting courses

# function to randomly make a scheule
def makeSchedule():
    schedule = []
    for course in courses:
        time = random.choice(timeAvail)
        hall = random.choice(halls)
        schedule.append((course,time,hall))
    return schedule

#function to initialize population
def initializePopulation(s):
    population = []
    for i in range(s):
        population.append(makeSchedule())
    return population

#function to calculate fitness conflicts in schedules
def fitness_COnflcts(conflicts, schedule,n):
    numConflicts = 0
    confctLst = []
    # print("Chromosome",n, " : ",schedule)
   
    # for schedules in schedule:
    for conflict in conflicts:
        for i in range(len(schedule)):
            if conflict[0] == schedule[i][0]:
                for j in range(len(schedule)):
                    if conflict[1] == schedule[j][0]:
                        if schedule[i][1] == schedule[j][1] and schedule[i][2] == schedule[j][2]:
                            # print("The following courses are conflicting: " , conflict)
                            # print("The conflicting timeslot: " , schedule[j][1] + " and the hall: " + schedule[i][2])
                            numConflicts += 1
                            # print()
                       
    #confctLst.append(numConflicts)
    # if(numConflicts == 0):
    #     print("No conflicts")
    #     print()

    return numConflicts

print()

#function to sum fitness values
def countFitness(fitnessList):
    fitnessSum = 0
    for i in range(len(fitnessList)):
        fitnessSum += fitnessList[i]
    return fitnessSum

#function to calculate fitness score of population
def fitnessScoreOfPopulation(population):
    fitnessList = []
    while True:
        for i in range(len(population)):
            for schedule in population:
                i+=1
                fitnessList.append(fitness_COnflcts(conflicts, schedule,i))
               # fitnessList.sort()
            return fitnessList


#sorting population with its corresponding fitness value to get the 2 best ones at start
def sortPopulation(population, fitnessList):
    for i in range(len(fitnessList)):
        for j in range(len(fitnessList)):
            if fitnessList[i] < fitnessList[j]:
                temp = fitnessList[i]
                fitnessList[i] = fitnessList[j]
                fitnessList[j] = temp
                temp = population[i]
                population[i] = population[j]
                population[j] = temp
    return population, fitnessList

#function to perform mutation
def MutatingPop(popp, mutationR):
    for schedule in popp:
        scheduleC = schedule.copy()
        randRate = random.random()
        # print("Random Mutation rate: " , randRate)
        if randRate < mutationR:
            print("Mutation occured")
            mutTime = random.choice(timeAvail)
            mutCourse = random.choice(courses)
            mutHall = random.choice(halls)
            for i in range(len(scheduleC)):
                if scheduleC[i][0] == mutCourse:
                    scheduleC[i] = (mutCourse, mutTime, mutHall)
                    # print("Before Mutation occured in chromosome: " , schedule)
                    # print("After Mutation occured in chromosome: " , scheduleC)
                    # print("The mutated course: " , mutCourse)
                    # print("The mutated timeslot: " , mutTime)
                    # print("The mutated hall: " , mutHall)
                    # print()

            print("Mutation didn't occur")
    return popp

#function to perform crossover
def CrossOver(popp1):
    #crossover
    offspp = []
    for i in range(len(popp1)):
        offspp1 =[]
        offspp2 =[]
        prob = random.random()
        # print("Probability of crossover: " , prob)
        if prob < 0.8:  #applying single-point crossover when prob is less than 0.8   
            cutPoint = random.randint(0, len(popp1[0])) #select a random crossover point
            offspp1 = popp1[0][0:cutPoint] + popp1[1][cutPoint:]
            offspp2 = popp1[1][0:cutPoint] + popp1[0][cutPoint:]
            offspp.append(offspp1)
            offspp.append(offspp2)
        else:
            offspp.append(popp1[0])
            offspp.append(popp1[1])   

    return offspp

#function to perform genetic algorithm
def GeneticAlgo(population, s):
    popp = population
    fitVal = []
    generations = []
    generationsFit = []

    # print()
    # print("Initial Population: " )
    # print(popp)

    #caluculating fitness value
    fitVal = fitnessScoreOfPopulation(popp)
    # print("Fitness value:" ,fitVal)
    # print()

    #sorting population according to fitness value
    # print()
    sortedpopp1, sortedfitVal = sortPopulation(popp, fitVal)
    # print("Sorted Population: " , sortedpopp1)
    # print("Sorted Fitness value:" ,sortedfitVal)
    
    gener = 100 
    for i in range(gener):
        print()
        print()
        print("Generation: " , i+1)
        print()
        newPoppu = []

        #selecting best 2 chromosomes for crossover
        print("Best 2 chromosomes for crossover chosen." )
        #print("Best 2 chromosomes for crossover: " , sortedpopp1[0:2] )
        # print()
        # print("and their fitness values " , sortedfitVal[0:2])
        # print()

        #crossover
        offsprings = []
        offsprings = CrossOver(sortedpopp1[0:2])
        print("Offsprings Created." )
        # print(offsprings)
        # print()

        #combining offsprings with the rest of the population
        print("Combined the population with offsprings. " )
        newPoppu = popp[2:] + offsprings
        # print(popp)
        # print()

        #mutation
        mutationR = 0.1 #mutation rate given inn assignmnt
        mutPop = MutatingPop(popp, mutationR)
        print("Updated population after Mutation." )
        newPoppu = mutPop  #updating population
        # print(mutPop)

        #calculating fitness value of mutated population
        fitValNew = fitnessScoreOfPopulation(newPoppu)
        generationsFit.append([fitValNew])

        # print()
        sortNewpopp1, sortNewfitVal = sortPopulation(newPoppu, fitValNew)
        
        #append current population to  generation
        generations.append((sortNewpopp1))
        chunk_size = 10
        generations1 = [generations[mm:mm+chunk_size] for mm in range(0, len(generations), chunk_size)]
        # print(generations1)
        
    for i in range(len(generations)):
        # generation which has the best chromosome
        if fitness_COnflcts(conflicts, generations[i][0],i) == 0:
            print()
            print("************************************************************************************************************************")
            print()
            print("Solution found in generation: " , i+1)
            print("Fitness value of the generation " ,generationsFit[i])
            print("The best chromosome: " , generations[i][0])
            print("The fitness value of the best chromosome: " , fitness_COnflcts(conflicts, generations[i][0],i))
            print("The total fitness score of the generation is" , countFitness(generationsFit[i][0]))
            print()
            print("************************************************************************************************************************")
            break
        else:
            print("No solution found")
            break

#main driver function        
def main():

    s = 10 #population size
    population =initializePopulation(s)
    print("Initialized population")
    print()
    print("Calling Genetic Algorithm")
    GeneticAlgo(population, s)

if __name__ == "__main__":
    main()

#running time of the program
start_time = time.time()
main()
print("Time for program execution: %s s." % (time.time() - start_time))