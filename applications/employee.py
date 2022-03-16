# database of the employee as dictonary
#add number of employee as many inside the dictonary
employee_dict = {"5055652986856":"Carter","5055652932815":"Harry","5055652906670":"Jack"}# make dictonary of the employee
#employee_dict ={"5055652922571":"RPi Lora Hat","5055652922595":"RPi Barcode Reader","5055652921208":"Air Monitoring Breakout","5055652921185":"USB RTC"}
#employee_dict ={"5055652932815":"Book 1","5055652986856":"Book 2","8902442211216":"Book 3","8902442211230":"Book 4"}
#
def search(dec):
            if dec in employee_dict:#check the barcode is in dictonary, if it is present go to inside if statement 
                a = employee_dict[dec]#extract name from barcode using this line
                print(a)

                file=open('Library_books.txt',"r")#open the file in read the file
                file_read = file.read()
                if a in file_read:#check name is present in data.txt file
                    return "already present"
                else:#if the name is not present in data.txt file then append the name in the file(to avoid the duplication)
                    file=open('Library_books.txt',"a+")
                    file.write(a)
                    file.write('\r')#append next line to file
                    file.close()
                    return a
            else:#if barcode is not in dictonary then return False
                return False#return False
            
