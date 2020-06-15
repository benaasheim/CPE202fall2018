def weight_on_planets():                                                        
    ew = float(input("What do you weigh on earth? \n"))                          
    mw = ew * 0.38                                                               
    jw = ew * 2.34                                                               
    print("On Mars you would weigh", "{:>2.2f}".format(mw), "pounds.\nOn Jupiter you would weigh", "{:>2.2f}".format(jw), "pounds.")
if __name__ == '__main__':
    weight_on_planets()
