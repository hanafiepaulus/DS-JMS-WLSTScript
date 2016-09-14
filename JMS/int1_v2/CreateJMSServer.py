connect("weblogic", "welcome1", "t3://10.87.225.160:10101")
edit()
startEdit()

cd('/')
cmo.createJMSServer('int_esb1_v2_jms1')

cd('/Deployments/int_esb1_v2_jms1')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb1,Type=Server')], ObjectName))

cd('/')
cmo.createJMSServer('int_esb1_v2_jms2')

cd('/Deployments/int_esb1_v2_jms2')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb2,Type=Server')], ObjectName))

cd('/')
cmo.createJMSServer('int_esb1_v2_jms3')

cd('/Deployments/int_esb1_v2_jms3')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb3,Type=Server')], ObjectName))

cd('/')
cmo.createJMSServer('int_esb1_v2_jms4')

cd('/Deployments/int_esb1_v2_jms4')
set('Targets',jarray.array([ObjectName('com.bea:Name=int_esb1_v2_osb4,Type=Server')], ObjectName))

save()
activate()

