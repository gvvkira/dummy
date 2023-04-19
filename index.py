import os
import app_config as cfg 
from multiprocessing import Process
import paho.mqtt.client as paho

config = cfg.getconfig()
client= paho.Client()
client.username_pw_set(username="ES-MQTT", password="iota#re-mqtt39")
BROKER_ADDRESS = str(os.environ.get("BROKER_ADDRESS"))
if not BROKER_ADDRESS:
   BROKER_ADDRESS = config["BROKER_ADDRESS"]

print BROKER_ADDRESS
RUNTIME_ID = str(os.environ.get("OFFSET_ID"))
if not RUNTIME_ID:
   RUNTIME_ID = "1"

print RUNTIME_ID

unitId=str(os.environ.get("UNIT_ID"))
if unitId == None:
    print "No unit Id passed, exiting"
    exit()
print(unitId)


SERVICE_NAME=str(os.environ.get("SERVICE_FILE_NAME"))
if SERVICE_NAME == None:
    SERVICE_NAME="ALL"
print(SERVICE_NAME)

PAGE_SIZE=str(os.environ.get("PAGE_SIZE"))
if PAGE_SIZE == None:
    PAGE_SIZE=str(1000)
print(PAGE_SIZE)

path = r"./"

tasks = ['batch_basic_calc.py','calc_dp_dt_dif_ratio_valve.py', 'calc_min_avg_max_median_sum_and_or.py','calc_scl_non_winthr_winsum_thr_roc_roll_spike.py',"calc_thermodynamics.py", "batch_calc_plf_runhour.py","batch_complex_calc.py","batch_calc_boiler_avl.py","batch_calc_boiler_sfr.py","grate_shutdown_hourly_steamLoad.py","DeviationsLossCalTemplateCondVac.py","DeviationsLossCalTemplateFWTemp.py","DeviationsLossCalTemplateHotWellTemp.py","DeviationsLossCalTemplateMSPres.py","DeviationsLossCalTemplateMSTemp.py","batch_calc_boiler_tags.py","batch_calc_grate_tags.py","batch_calc_hourly_params_heating.py","batch_calc_hourly_params_TBWES.py","batch_calc_powerRating_steamLoadPercent.py","batch_calc_prev_day_avg.py","manualTagsPublisher.py","manualtag_backfilling.py"]


def foo(task):
    # print ('UNIT_ID='+unitId+' '+'BROKER_ADDRESS='+BROKER_ADDRESS+' python ' + path + task + ' > /tmp/log/'+unitId+'/data-calculation-b/'+task+'.log &2>1')
    #os.system('UNIT_ID='+unitId+' '+'BROKER_ADDRESS='+BROKER_ADDRESS+' python ' + path + task + ' > /tmp/log/'+unitId+'/data-calculation-b/'+task+'.log &2>1')
    # os.system('RUNTIME_ID='+RUNTIME_ID+' UNIT_ID='+unitId+' '+'BROKER_ADDRESS='+BROKER_ADDRESS+' python ' + path + task+ ' > /tmp/log/'+unitId+'/data-calculation-b/'+task+'.log &2>1')
    print('RUNTIME_ID='+RUNTIME_ID+' UNIT_ID='+unitId+' '+'LAS=yes PAGE_SIZE='+PAGE_SIZE+' '+'BROKER_ADDRESS='+BROKER_ADDRESS+' python ' + path + task)
    os.system('RUNTIME_ID='+RUNTIME_ID+' UNIT_ID='+unitId+' '+'LAS=yes PAGE_SIZE='+PAGE_SIZE+' '+'BROKER_ADDRESS='+BROKER_ADDRESS+' python ' + path + task)

for task in tasks:
    if (SERVICE_NAME=="ALL") or (SERVICE_NAME==task):
        print(task,"********")
        p = Process(target=foo, args=(task,))
        p.start()

