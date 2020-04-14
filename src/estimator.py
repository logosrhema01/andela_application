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
    def mainData(self):
        return self.name,self.avgAge,self.avgDailyIncomeInUSD,self.avgDailyIncomePopulation,self.periodType,self.timeToElapse,self.reportedCases,self.popultion,self.totalHospitalBeds
ghana=inputData("Ghana")
ghana.regionInputData(19.7,5,0.71)
ghana.inputData2("days",58,674,66622705,1380614)
print(ghana.mainData())
def estimator(input_data):
    input_data()
    impact()
    sever
    return data
