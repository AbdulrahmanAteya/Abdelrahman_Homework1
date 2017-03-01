from __future__ import print_function, division
import nsfg


#Q1

pres = nsfg.ReadFemResp()


#Q2

pres.head(20)
pres.tail(30)
pres.columns
countcolumns = 0
countrows = 0
for columns in pres:
    countcolumns = countcolumns+1
for rows in pres.agescrn:
    countrows=countrows+1
print ("There are %d rows and %d columns"%(countrows, countcolumns))


#Q3

oldest=0
youngest=10000
for values in pres.agescrn:
    if values >= oldest:
         oldest = values
    if values <= youngest:
        youngest =values
    else:
        pass
print ("The oldest is %d years old"%oldest)
print ("The youngest is %d years old"%youngest)


#Q4

checker=0
for values in pres.numpregs:
    if checker == 2298:
        print (str(values)+" Pregnancies")
    #print (pres[pres.caseid==2298])
    else:
        pass
    checker += 1


#Q5

under25 = pres[(pres['agescrn']<= 25)]
mean = under25['pregnum']
print (mean.mean())



#Q6

years44 = pres[(pres['agescrn'] == 44)]
mean44 = years44['pregnum']
print (mean44.mean())





            








