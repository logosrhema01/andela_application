'Code cotains Option For User TO Input Data and I added Classes to make the Code more Flexible'



class inputData:
    def __init__(self,name):
        self.name=name

    def regionInputData(self,avgAge,avgDailyIncomeInUSD,avgDailyIncomePopulation):
            self.avgAge=avgAge
            self.avgDailyIncomeInUSD=avgDailyIncomeInUSD
            self.avgDailyIncomePopulation=avgDailyIncomePopulation
    
    def getRegionInputData(self):
            return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation
    
    def inputData2(self,periodType,timeToElapse,reportedCases,population,totalHospitalBeds):
            self.periodType=periodType
            self.timeToElapse=timeToElapse
            self.reportedCases=reportedCases
            self.popultion=population
            self.totalHospitalBeds=totalHospitalBeds
            
    def getInputData2(self):
        return self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds
    
    def mainInputData(self):
        return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation,self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds




'Inheriting From Input Data'
class estimator(inputData):
    def currentlyInfected(self):
        impactA=self.reportedCases*10
        severeImpactA=self.reportedCases*50
        return "Impact: ",int(impactA),"Severe Impact:",(severeImpactA)
    
    def infectionsByRequestedTime(self,increaseDays):
        self.increaseDays=increaseDays
        impactB=self.reportedCases*10*increaseDays
        severeImpactB=self.reportedCases*50*increaseDays
        return "Impact: ",int(impactB),"Severe Impact:",(severeImpactB)

    def severeCasesByRequestedTime(self):
        severeImpactB=self.reportedCases*50*self.increaseDays
        severeCasesBRT=severeImpactB/(15/100)
        return int(severeCasesBRT)

    def hospitalBedsByRequestedTime(self):
        severeCasesBRT=(self.reportedCases*50*self.increaseDays)/(15/100)
        bedsforSeverePatients=(self.totalHospitalBeds)/(35/100)
        bedsAvailable=bedsforSeverePatients-severeCasesBRT
        return int(bedsAvailable)

    def casesForICUByRequestedTime(self):
        severeImpactB=self.reportedCases*50*self.increaseDays
        ICUcare=severeImpactB/(5/100)
        return int(ICUcare)

    def casesForVentilatorsByRequestedTime(self):
        severeImpactB=self.reportedCases*50*self.increaseDays
        requireVentilators=severeImpactB/(2/100)
        return int(requireVentilators)

    def dollarsInFlight(self):
        severeImpactB=self.reportedCases*50*self.increaseDays
        loss=(severeImpactB * 0.65 * 1.5)/30
        return int(loss)




'Inputs Come Here'
input()
ghana=estimator("Ghana")
ghana.regionInputData(19.7,5,0.71)
ghana.inputData2("days",58,674,66622705,1380614)
togo=estimator("Togo")
togo.regionInputData(19.7,5,0.71)
togo.inputData2("days",58,100,66622705,1380614)



'Outputing The Estimations'

ghana.infectionsByRequestedTime(512)
togo.infectionsByRequestedTime(2)
print(ghana.severeCasesByRequestedTime())
print(togo.severeCasesByRequestedTime())
print(ghana.hospitalBedsByRequestedTime())
togo.hospitalBedsByRequestedTime()