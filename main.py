import RPi.GPIO as GPIO
from time import sleep
from flask import *
import threading
import os
import time
import Adafruit_DHT
import cv2
from picamera2 import Picamera2
picam = Picamera2()
picam.preview_configuration.main.size = (480, 480)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.main.align()
picam.configure("preview")
picam.start()
dht_pin = 4

stat_led=20
data_led=16

TRIG=17
ECHO=27
gas=19
m1_f=6
m1_r=5
buzzer=13

servo_pin = 22
servo_pin1 = 23

humidity=0
temperature=0
distance=0
gas_val=""
datas=""

sensor = Adafruit_DHT.DHT11

app=Flask(__name__)
@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/control',methods=['post'])
def control():
    global datas
    global voice
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
    # Start PWM with 0% duty cycle (servo at 0 degrees)
    pwm2 = GPIO.PWM(servo_pin1, 50)
    pwm.start(0)
    pwm2.start(0)
    try:
        rec_data=request.form['data']
        print(rec_data)
        if rec_data=='A':
            GPIO.output(m1_f,True)
            GPIO.output(m1_r,False)
            time.sleep(1)
            GPIO.output(m1_f,False)
            GPIO.output(m1_r,False)
            rec_data=''
        elif rec_data=='B':
            GPIO.output(m1_f,False)
            GPIO.output(m1_r,True)
            time.sleep(1)
            GPIO.output(m1_f,False)
            GPIO.output(m1_r,False)
            rec_data=''
        elif rec_data == 'C':
            pwm.ChangeDutyCycle(2.5)
            time.sleep(1)
            rec_data = ''
        elif rec_data == 'D':
            pwm.ChangeDutyCycle(7.5)
            time.sleep(1)
            rec_data = ''
        elif rec_data == 'E':
            pwm2.ChangeDutyCycle(2.5)
            time.sleep(1)
            rec_data = ''
        elif rec_data == 'F':
            pwm2.ChangeDutyCycle(7.5)
            time.sleep(1)
            rec_data = ''
        return jsonify({'result':'success'})
        GPIO.output(data_led,True)
        time.sleep(0.4)
        GPIO.output(data_led,False)
        time.sleep(0.4)
    except Exception as e:
        return jsonify({'result':'error'})


@app.route('/sensor_reading',methods=['GET','POST'])
def sensor_reading():
    global distance
    global temperature
    global humidity
    global gas_val
    try:
        v=request.form['lid']
        print(v)
        return jsonify({'result':'success','temp':str(temperature),'humidity':str(humidity),'gas':str(gas_val),'dist':str(distance)})
    except Exception as e:
        print(e)      
        return jsonify({'result':'error'})
@app.route('/view_comments',methods=['GET','POST'])
def view_comments():
    global datas
    d=""
    if datas:
        d=datas
        datas=""
    return jsonify({'result':'success','comment':str(d)})

def generate_frames():
    while True:
        frame = picam.capture_array()
        
        # Encode the frame as JPEG
        success, buffer = cv2.imencode('.jpg', frame)
        if not success:
            continue
        
        # Convert the buffer to bytes
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')    
        
            

def main():
    global distance
    global temperature
    global humidity
    global gas_val
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(m1_f,GPIO.OUT)
    GPIO.setup(m1_r,GPIO.OUT)
    GPIO.setup(stat_led,GPIO.OUT)
    GPIO.setup(data_led,GPIO.OUT)
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(gas,GPIO.IN)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.setup(servo_pin1, GPIO.OUT)
    GPIO.output(m1_f,False)
    GPIO.output(m1_r,False)
    threading.Thread(target=generate_frames).start()
    threading.Thread(target=check).start()
    threading.Thread(target=connect).start()
def check():
    global distance
    global temperature
    global humidity
    global gas_val
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        if humidity is not None and temperature is not None:
              print("Temperature: {:.1f}°C | Humidity: {}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from sensor!")
        gas_va=GPIO.input(gas)
        if gas_va==0:
            gas_val="HIGH"
            print("GAS HIGH")

        if gas_va==1:
            gas_val="LOW"
            print("GAS LOW")

        GPIO.output(TRIG, False)
        time.sleep(0.00001)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(ECHO) == 0:
            StartTime = time.time()
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        print(distance)
        if (distance<=20):
            print("alert")
            GPIO.output(buzzer,True)
            time.sleep(1)
            GPIO.output(buzzer,False)
 
            


        
        
def connect():
    app.run(host="0.0.0.0",port=5000)

if __name__=="__main__":
    main()
