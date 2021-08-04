from datetime import datetime
import pytz

from pytz import timezone

from src.data import DATA


class APP():

    def __init__(self,period,timezone,point1,point2):
        
        self.to_UTC = 'UTC'
        self.date_form = '%Y%m%dT%H%M%SZ'

        #ptlist input
        self.logs = DATA.ptlist_o 
       
        try:
            #t1 input
            self.point1 = datetime.strptime(point1, self.date_form)
            #t2 input           
            self.point2 = datetime.strptime(point2, self.date_form)            
            
        except ValueError:
            raise ('ERROR Incorrect data type format please use YYmmddTHHMMSSZ format" ')
    
        if self.point1 >= self.point2:
                raise ValueError("ERROR t1 must be less than t2") 

        #Assign every supported period to the respective formatter function
        self.period_map = {'1h':self.hour_format,'1d':self.day_format,'1mo':self.month_format,'1y':self.year_format}
       
        if period not in self.period_map:
            raise ValueError("EROOR Unsupported period")
        #period input
        self.period = period
        
        if timezone not in pytz.all_timezones:
            raise ValueError("ERROR Incorrect TimeZone")
        #timezone input
        self.from_UTC = timezone      
        



    def localize(self,date,utc):
        
        #Convert timezone-unaware to timezone-aware
        converted = timezone(utc).localize(date)
        return converted


    
    def conv_tz(self,date,source_utc,target_utc):
       
        #Localize date to source UTC 
        converted =  self.localize(date,source_utc)
        #Convert to the target UTC
        converted = converted.astimezone(pytz.timezone(target_utc))
        return converted


 
    def find_matches(self):        
        
        self.lst = []
        #Search logs, find any match and append it in self.lst
        for key,item in enumerate(self.logs):
            #Make appropriate conversion in order to compare same type of dates
            t1 = self.conv_tz(self.point1,self.from_UTC,self.to_UTC)
            t2 = self.conv_tz(self.point2,self.from_UTC,self.to_UTC)
            
            #Validate log data format and make it timezone-aware
            try:
                log = self.localize(datetime.strptime(item, self.date_form),self.to_UTC)
            except ValueError:
                raise ValueError('ERROR during reading logs from ptlist Incorrect data format ')

            if  t1 < log < t2:
                                                   #revesrse conversion
                self.lst.append(log.astimezone(pytz.timezone(self.from_UTC)))

        

    def run(self):
        
        #Find matches
        self.find_matches()
        #Chosse the appropriate formatter regarding period
        formatter = self.period_map[self.period]              
        formatter()
        #Print results converted in UTC +00         
        for i in self.lst:
            val =i.astimezone(pytz.timezone('UTC'))
            print(val.replace(tzinfo=None)) 

    #Implematation of formatters depending period input
    def hour_format(self):
        
        for key,item in enumerate(self.lst):
            self.lst[key] = item.replace(minute=0,second=0)       
        
        self.lst = set(self.lst)   

    def day_format(self):
        
         for key,item in enumerate(self.lst):
            self.lst[key] = item.replace(hour=0,minute=0,second=0)
        
         self.lst = set(self.lst)

    def month_format(self):
       
        for key,item in enumerate(self.lst):
            self.lst[key] = item.replace(day=1,hour=0,minute=0,second=0)   
        
        self.lst = set(self.lst)

    def year_format(self):
       
        for key,item in enumerate(self.lst):
            self.lst[key] = item.replace(month=1,day=1,hour=0,minute=0,second=0)   
        
        self.lst = set(self.lst) 



