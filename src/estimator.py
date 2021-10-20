


class inputData:
    def __init__(self,name):
        self.name=name

    def regionInputData(self,avgAge,avgDailyIncomeInUSD,avgDailyIncomePopulation,periodType,timeToElapse,reportedCases,population,totalHospitalBeds):
        self.avgAge=avgAge
        self.avgDailyIncomeInUSD=avgDailyIncomeInUSD
        self.avgDailyIncomePopulation=avgDailyIncomePopulation
        self.periodType=periodType
        self.timeToElapse=timeToElapse
        self.reportedCases=reportedCases
        self.popultion=population
        self.totalHospitalBeds=totalHospitalBeds
        return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation,self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds
    
    def mainInputData(self):
        return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation,self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds




'Inheriting From Input Data'
class estimator(inputData):
    def currentlyInfected(self):
        impactA=self.reportedCases*10
        severeImpactA=self.reportedCases*50
        return impactA,severeImpactA
    
    def infectionsByRequestedTime(self,increaseDays):
        self.increaseDays=increaseDays
        impactB=self.reportedCases*10*increaseDays
        severeImpactB=self.reportedCases*50*increaseDays
        return impactB,severeImpactB

    def severeCasesByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*self.increaseDays)
        severeCasesBRT=severeImpactB/(15/100)
        return (severeCasesBRT)

    def hospitalBedsByRequestedTime(self):
        severeCasesBRT=int(self.reportedCases*50*self.increaseDays)/(15/100)
        bedsforSeverePatients=int(self.totalHospitalBeds)/(35/100)
        bedsAvailable=bedsforSeverePatients-severeCasesBRT
        return (bedsAvailable)

    def casesForICUByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*self.increaseDays)
        ICUcare=severeImpactB/(5/100)
        return (ICUcare)

    def casesForVentilatorsByRequestedTime(self):
        severeImpactB=int(self.reportedCases*50*self.increaseDays)
        requireVentilators=severeImpactB/(2/100)
        return (requireVentilators)

    def dollarsInFlight(self):
        severeImpactB=int(self.reportedCases*50*self.increaseDays)
        loss=(severeImpactB * 0.65 * 1.5)/30
        return (loss)


