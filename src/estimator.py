


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


AverageAge=0
AverageDailyIncomeInUSD=0
AverageDailyIncomeofPopulation=0
TimetoElapse=0
ReportedCases=0
Population=0
TotalHospitalBeds=0
DaysitDoubles=0




'Inputs Come Here'




class  inputoutputdetails(estimator):
    def setregionName(self,Region):
        self.Region=Region
        return Region

    def getRegion(self):
        return self.Region

    def setAverageAgeIn(self,AverageAge):
        self.AverageAge=AverageAge
        return AverageAge

    def getAverageAgeIn(self):
        return self.AverageAge


    def setAverageDailyIncomeInUSDIn(self,AverageDailyIncomeInUSD):
        self.AverageDailyIncomeInUSD=AverageDailyIncomeInUSD
        return AverageDailyIncomeInUSD

    def getAverageDailyIncomeInUSDIn(self):
        return self.AverageDailyIncomeInUSD
    
    
    def setAverageDailyIncomeofPopulationIn(self,AverageDailyIncomeofPopulation):
        self.AverageDailyIncomeofPopulation=AverageDailyIncomeofPopulation
        return AverageDailyIncomeofPopulation

    def getAverageDailyIncomeofPopulationIn(self):
        return self.AverageDailyIncomeofPopulation


    def setPeriodTypeIn(self,PeriodType):
        self.PeriodType=PeriodType
        return PeriodType

    def getPeriodTypeIn(self):
        return self.PeriodType


    def setTimetoElapseIn(self,TimetoElapse):
        self.TimetoElapse=TimetoElapse
        return TimetoElapse

    def getTimetoElapseIn(self):
        return self.TimetoElapse


    def setReportedCasesIn(self,ReportedCases):
        self.ReportedCases=ReportedCases
        return ReportedCases

    def getReportedCasesIn(self):
        return self.ReportedCases


    def setPopulationIn(self,Population):
        self.Population=Population
        return Population

    def getPopulationIn(self):
        return self.Population


    def setTotalHospitalBedsIn(self,TotalHospitalBeds):
        self.TotalHospitalBeds=TotalHospitalBeds
        return TotalHospitalBeds

    def getTotalHospitalBedsIn(self):
        return self.TotalHospitalBeds


    def setDaysitDoublesIn(self,DaysitDoubles):
        self.DaysitDoubles=DaysitDoubles
        return DaysitDoubles

    def getDaysitDoublesIn(self):
        return self.DaysitDoubles




    
    def setregionInData(self):
        return estimator(self.Region).regionInputData(self.AverageAge,self.AverageDailyIncomeInUSD,self.AverageDailyIncomeofPopulation,self.PeriodType,self.TimetoElapse,self.ReportedCases,self.Population,self.TotalHospitalBeds)
    
    def setcurrentlyInfectedOutfunc(self):
        return estimator(self.Region).currentlyInfected()
    
    def setinfectionsByRequestedTimeOutfunc(self):
        return estimator(self.Region).infectionsByRequestedTime(((self.ReportedCases)/(2**(self.TimetoElapse/(self.DaysitDoubles)))))
    
    def setsevereCasesByRequestedTimeOutfunc(self):
        return estimator(self.Region).severeCasesByRequestedTime()
    
    def sethospitalBedsByRequestedTImeOutfunc(self):
        return estimator(self.Region).hospitalBedsByRequestedTime()
    
    def setcasesForICUByRequestedTimeOutfunc(self):
        return estimator(self.Region).casesForICUByRequestedTime()
   
    def setcasesForVentilatorsOutfunc(self):
        return estimator(self.Region).casesForVentilatorsByRequestedTime()
    
    def setdollarsInFlightOutfunc(self):
        return estimator(self.Region).dollarsInFlight()



    def getregionName(self):
        return estimator(self.Region)

    def getregionInData(self):
        return estimator(self.Region).regionInputData(self.AverageAge,self.AverageDailyIncomeInUSD,self.AverageDailyIncomeofPopulation,self.PeriodType,self.TimetoElapse,self.ReportedCases,self.Population,self.TotalHospitalBeds)
    
    def getcurrentlyInfectedOutfunc(self):
        return estimator(self.Region).currentlyInfected()

    def getinfectionsByRequestedTimeOutfunc(self):
        return estimator(self.Region).infectionsByRequestedTime(((self.ReportedCases)/(2**(self.TimetoElapse/(self.DaysitDoubles)))))

    def getsevereCasesByRequestedTimeOutfunc(self):
        return estimator(self.Region).severeCasesByRequestedTime()

    def gethospitalBedsByRequestedTImeOutfunc(self):
        return estimator(self.Region).hospitalBedsByRequestedTime()

    def getcasesForICUByRequestedTimeOutfunc(self):
        return estimator(self.Region).casesForICUByRequestedTime()

    def getcasesForVentilatorsOutfunc(self):
        return estimator(self.Region).casesForVentilatorsByRequestedTime()

    def getdollarsInFlightOutfunc(self):
        return estimator(self.Region).dollarsInFlight()