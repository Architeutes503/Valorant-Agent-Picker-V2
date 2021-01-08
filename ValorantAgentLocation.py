import pyautogui
import time

#Explanation    
print("This programm saves the location of all the agents and the lock in button.")
print("The locations get saved in a .txt file in the same folder as this python file is.")
print("To use it copy the location.txt file into the same folder as the ValorantAgentPicker.py is located in.")


#Breach
print("Please hover your cursor over Breach and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(5)
breachMouseX, breachMouseY = pyautogui.position()
pyautogui.alert("Done.(Breach)")


#Brimstone
print("Please hover your cursor over Brimstone and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
brimstoneMouseX, brimstoneMouseY = pyautogui.position()
pyautogui.alert("Done.(Brimstone)")


#Cypher
print("Please hover your cursor over Cypher and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
cypherMouseX, cypherMouseY = pyautogui.position()
pyautogui.alert("Done.(Cypher)")


#Jett
print("Please hover your cursor over Jett and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
jettMouseX, jettMouseY = pyautogui.position()
pyautogui.alert("Done.(Jett)")


#Killjoy
print("Please hover your cursor over Killjoy and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
killjoyMouseX, killjoyMouseY = pyautogui.position()
pyautogui.alert("Done.(Killjoy)")


#Omen
print("Please hover your cursor over Omen and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
omenMouseX, omenMouseY = pyautogui.position()
pyautogui.alert("Done.(Omen)")


#Phoenix
print("Please hover your cursor over Phoenix and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
phoenixMouseX, phoenixMouseY = pyautogui.position()
pyautogui.alert("Done.(Phoenix)")


#Raze
print("Please hover your cursor over Raze and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
razeMouseX, razeMouseY = pyautogui.position()
pyautogui.alert("Done.(Raze)")


#Reyna
print("Please hover your cursor over Reyna and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
reynaMouseX, reynaMouseY = pyautogui.position()
pyautogui.alert("Done.(Reyna)")


#Sage
print("Please hover your cursor over Sage and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
sageMouseX, sageMouseY = pyautogui.position()
pyautogui.alert("Done.(Sage)")


#Skye
print("Please hover your cursor over Skye and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
skyeMouseX, skyeMouseY = pyautogui.position()
pyautogui.alert("Done.(Skye)")


#Sova
print("Please hover your cursor over Sova and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
sovaMouseX, sovaMouseY = pyautogui.position()
pyautogui.alert("Done.(Sova)")


#Viper
print("Please hover your cursor over Viper and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
viperMouseX, viperMouseY = pyautogui.position()
pyautogui.alert("Done.(Viper)")

#LockIn
print("Please hover your cursor over the lock in Button and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
lockMouseX, lockMouseY = pyautogui.position()
pyautogui.alert("Done.(LockIn)")


locations = open("locations.txt", "w")



#Breach
locations.write(str(breachMouseX))
locations.write("\n")
locations.write(str(breachMouseY))
locations.write("\n")


#Brimstone
locations.write(str(brimstoneMouseX))
locations.write("\n")
locations.write(str(brimstoneMouseY))
locations.write("\n")


#Cypher
locations.write(str(cypherMouseX))
locations.write("\n")
locations.write(str(cypherMouseY))
locations.write("\n")


#Jett
locations.write(str(jettMouseX))
locations.write("\n")
locations.write(str(jettMouseY))
locations.write("\n")


#Killjoy
locations.write(str(killjoyMouseX))
locations.write("\n")
locations.write(str(killjoyMouseY))
locations.write("\n")


#Omen
locations.write(str(omenMouseX))
locations.write("\n")
locations.write(str(omenMouseY))
locations.write("\n")

#Phoenix
locations.write(str(phoenixMouseX))
locations.write("\n")
locations.write(str(phoenixMouseY))
locations.write("\n")


#Raze
locations.write(str(razeMouseX))
locations.write("\n")
locations.write(str(razeMouseY))
locations.write("\n")


#Reyna
locations.write(str(reynaMouseX))
locations.write("\n")
locations.write(str(reynaMouseY))
locations.write("\n")


#Sage
locations.write(str(sageMouseX))
locations.write("\n")
locations.write(str(sageMouseY))
locations.write("\n")


#Skye
locations.write(str(skyeMouseX))
locations.write("\n")
locations.write(str(skyeMouseY))
locations.write("\n")


#Sova
locations.write(str(sovaMouseX))
locations.write("\n")
locations.write(str(sovaMouseY))
locations.write("\n")


#Viper
locations.write(str(viperMouseX))
locations.write("\n")
locations.write(str(viperMouseX))
locations.write("\n")


#LockIn
locations.write(str(lockMouseX))
locations.write("\n")
locations.write(str(lockMouseY))
locations.write("\n")