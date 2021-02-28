##Downloaded PyCharm as my tool of use
###Created the project
##Downloaded pandas library
#Importing pandas library
import pandas as pd #For data manipulation
import geopandas as gp #For polygons and signals cross reference
from shapely import wkt #For formating poligons
import glob #For importing files

#Stepse followed for the solution
#1. Creating a full affinity table for all the users

###Importing the affinity files & adding their affinity positivity
###Addidas
addidas=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/addidas",names=["device_id"])
    #Adding addidas value
addidas["addidas"]=1
###Apple
apple=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/apple",names=["device_id"])
    #Adding apple value
apple["apple"]=1
###Bmw
bmw=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/bmw",names=["device_id"])
    #Adding bmw value
bmw["bmw"]=1
###Employed
employed=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/employed",names=["device_id"])
    #Adding employed value
employed["employed"]=1
###Female
female=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/female",names=["device_id"])
    #Adding female value
female["female"]=1
###H_&_m
h_and_m=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/h_&_m",names=["device_id"])
    #Adding h_&_m value
h_and_m["h_&_m"]=1
###High_income
high_income=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/high_income",names=["device_id"])
    #Adding high_income value
high_income["high_income"]=1
###Honda
honda=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/honda",names=["device_id"])
    #Adding honda value
honda["honda"]=1
###Job_seeking
job_seeking=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/job_seeking",names=["device_id"])
    #Adding job_seeking value
job_seeking["job_seeking"]=1
###Low_income
low_income=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/low_income",names=["device_id"])
    #Adding low_income value
low_income["low_income"]=1
###Male
male=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/male",names=["device_id"])
    #Adding male value
male["male"]=1
###Mercedes-benz
mercedes_benz=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/mercedes-benz",names=["device_id"])
    #Adding mercedes-benz value
mercedes_benz["mercedes-benz"]=1
###Middle_income
middle_income=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/middle_income",names=["device_id"])
    #Adding middle_income value
middle_income["middle_income"]=1
###Retired
retired=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/retired",names=["device_id"])
    #Adding retired value
retired["retired"]=1
###Student
student=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/student",names=["device_id"])
    #Adding student value
student["student"]=1
###Tommy_helfinger
tommy_helfinger=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/affinities/tommy_helfinger",names=["device_id"])
    #Adding tommy_helfinger value
tommy_helfinger["tommy_helfinger"]=1

####As we imported all the necessary information, now we merge the info together
#First we take all the existing users id  and make all them unique
#Adding addidas users
all_affinity_users=addidas[["device_id"]].copy()
#Adding apple users
all_affinity_users=all_affinity_users.append(apple[["device_id"]].copy())
#Adding bmw users
all_affinity_users=all_affinity_users.append(bmw[["device_id"]].copy())
#Adding employed users
all_affinity_users=all_affinity_users.append(employed[["device_id"]].copy())
#Adding female users
all_affinity_users=all_affinity_users.append(female[["device_id"]].copy())
#Adding h_and_m users
all_affinity_users=all_affinity_users.append(h_and_m[["device_id"]].copy())
#Adding high_income users
all_affinity_users=all_affinity_users.append(high_income[["device_id"]].copy())
#Adding honda users
all_affinity_users=all_affinity_users.append(honda[["device_id"]].copy())
#Adding job_seeking users
all_affinity_users=all_affinity_users.append(job_seeking[["device_id"]].copy())
#Adding low_income users
all_affinity_users=all_affinity_users.append(low_income[["device_id"]].copy())
#Adding male users
all_affinity_users=all_affinity_users.append(male[["device_id"]].copy())
#Adding mercedes_benz
all_affinity_users=all_affinity_users.append(mercedes_benz[["device_id"]].copy())
#Adding middle_income
all_affinity_users=all_affinity_users.append(middle_income[["device_id"]].copy())
#Adding retired
all_affinity_users=all_affinity_users.append(retired[["device_id"]].copy())
#Adding student
all_affinity_users=all_affinity_users.append(student[["device_id"]].copy())
#Adding tommy_helfinger
all_affinity_users=all_affinity_users.append(tommy_helfinger[["device_id"]].copy())
###Now that we have added all the users from afinity we drop the duplicates and keep
#only the unique values
all_affinity_users.drop_duplicates(inplace=True)
###Now that we have the unique users we can add their fully KYC list

#Adding addidas
all_affinity_users=pd.merge(all_affinity_users,addidas,on="device_id",how="left")
#Adding apple users
all_affinity_users=pd.merge(all_affinity_users,apple,on="device_id",how="left")
#Adding bmw users
all_affinity_users=pd.merge(all_affinity_users,bmw,on="device_id",how="left")
#Adding employed users
all_affinity_users=pd.merge(all_affinity_users,employed,on="device_id",how="left")
#Adding female users
all_affinity_users=pd.merge(all_affinity_users,female,on="device_id",how="left")
#Adding h_and_m users
all_affinity_users=pd.merge(all_affinity_users,h_and_m,on="device_id",how="left")
#Adding high_income users
all_affinity_users=pd.merge(all_affinity_users,high_income,on="device_id",how="left")
#Adding honda users
all_affinity_users=pd.merge(all_affinity_users,honda,on="device_id",how="left")
#Adding job_seeking users
all_affinity_users=pd.merge(all_affinity_users,job_seeking,on="device_id",how="left")
#Adding low_income users
all_affinity_users=pd.merge(all_affinity_users,low_income,on="device_id",how="left")
#Adding male users
all_affinity_users=pd.merge(all_affinity_users,male,on="device_id",how="left")
#Adding mercedes_benz
all_affinity_users=pd.merge(all_affinity_users,mercedes_benz,on="device_id",how="left")
#Adding middle_income
all_affinity_users=pd.merge(all_affinity_users,middle_income,on="device_id",how="left")
#Adding retired
all_affinity_users=pd.merge(all_affinity_users,retired,on="device_id",how="left")
#Adding student
all_affinity_users=pd.merge(all_affinity_users,student,on="device_id",how="left")
#Adding tommy_helfinger
all_affinity_users=pd.merge(all_affinity_users,tommy_helfinger,on="device_id",how="left")

###Feeling with zero the NA values
all_affinity_users.fillna(value=0,inplace=True)

###Now we have a full KYC of all the users

##The second step is, merging the kyc to each signal, also  allocating whether a signal belongs into a polygon or not
#First we import all the signals and merge them in one
###Signals

###First we import and merge all the signals and also format date
#The way to import all data
signal_path = r'C:/Users/User/OneDrive/Pictures/Kevin/sample_data'
all_files = glob.glob(signal_path + "/*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

signals = pd.concat(li, axis=0, ignore_index=True)


# signals=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/full_data/part_57.csv") this ose done for sample data
signals=pd.DataFrame(signals)
#Change the timestamp to date timer
signals["date"]=pd.to_datetime(signals.utc_timestamp, unit='ms')
signals["date"]=signals["date"].dt.date
signals=pd.DataFrame(signals)

#Adding the kyc to each sinal
signals=pd.merge(signals,all_affinity_users,on="device_id",how="left")
#Formating signal into a point
signals_formatted=gp.GeoDataFrame(signals,geometry=gp.points_from_xy(signals.lon, signals.lat))

# We import stores  format them
stores=pd.read_csv("C:/Users/User/OneDrive/Pictures/Kevin/stores.csv")
stores["wkt"]=stores["wkt"].apply(wkt.loads) #To make it computable

stores_formatted=gp.GeoDataFrame(stores).set_geometry('wkt') #Making stores in a computable format

##After we made the needed forma, we can check to each store the signal belings
signal_store=gp.sjoin(signals_formatted,stores_formatted, how="left", op='within')
##Now we have what we need, hence we filter relevant data for data processing
signal_store_formatted=signal_store[["device_id","date","addidas","apple","bmw","employed","female","h_&_m","high_income","honda","job_seeking","low_income","male","mercedes-benz","middle_income","retired","student","tommy_helfinger","geometry","store_id","store_name"]].copy()
#We add a datecode in order to make it easier for manipulation of data
signal_store_formatted["date_code"]=pd.DatetimeIndex(signal_store_formatted["date"]).day.astype(str)+pd.DatetimeIndex(signal_store_formatted["date"]).month.astype(str)+pd.DatetimeIndex(signal_store_formatted["date"]).year.astype(str)

#Since our focus is in store only, we do not need the signals that belong to any store
signal_store_formatted=pd.DataFrame(signal_store_formatted)
signal_store_formatted=signal_store_formatted[signal_store_formatted['store_id'].notna()]
#We add anew column "visitro" to ease the calculations
signal_store_formatted["visitor"]=1

#Now we have what we need
##Frist we select the key columns which are necessary for us
signal_store_final=signal_store_formatted[["date","date_code","store_id","store_name"]].copy()
#Second we drop duplicates and keep only unique combinations
signal_store_final.drop_duplicates(subset=["date_code","store_id","store_name"],inplace=True)
###Adding the total signals by store and date
total_signals=pd.pivot_table(signal_store_formatted,index=["date_code","store_id","store_name"],values="visitor",aggfunc="sum")
total_signals.reset_index(inplace=True)
total_signals.rename(columns={"visitor":"total_signals"},inplace=True)
signal_store_final=pd.merge(signal_store_final,total_signals,on=["date_code","store_id","store_name"],how="left")
#To make the unique values for every other detail first we need to drop duplicates
daily_unique_signals=signal_store_formatted.copy()
daily_unique_signals.drop_duplicates(subset=["date_code","store_id","store_name","device_id"],inplace=True)

daily_unique_signals_summary=pd.pivot_table(daily_unique_signals,index=["date_code","store_id","store_name"],
                                            values=["visitor","addidas","apple","bmw","employed","female","h_&_m","high_income",
                                                    "honda","job_seeking","low_income","male","mercedes-benz",
                                                    "middle_income","retired","student","tommy_helfinger"],aggfunc="sum")
daily_unique_signals_summary.reset_index(inplace=True)
daily_unique_signals_summary.rename(columns={"visitor":"unique_visits"},inplace=True)
signal_store_final=pd.merge(signal_store_final,daily_unique_signals_summary,on=["date_code","store_id","store_name"],how="left")
signal_store_final.fillna(value=0,inplace=True)

# print(signal_store)
# signal_store=pd.DataFrame(signal_store)
#Saving it in excel file
writer = pd.ExcelWriter('C:/Users/User/OneDrive/Pictures/Kevin/check123.xlsx', engine='xlsxwriter')

signal_store_final.to_excel(writer,sheet_name="Final")

writer.save()

# stores_formatted=Polygon(store
# s.wkt[1])
# print(stores_formatted)
# stores_formatted=gp.GeoDataFrame(stores,geometry=gp.points_from_xy(df.Longitude, df.Latitude))
# stores.plot()
# print(type(stores))



