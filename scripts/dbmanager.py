import sys

def ReadSettings():
    import configparser
    config = configparser.ConfigParser()
    settings = config.read('settings.ini')
    if 'DATABASE' in config:
        global dbset
        dbset = config['DATABASE']
        del configparser
    else:
        log("Settings File Not Found.")

def DBConnection():
    if dbset['DBServer'] not in ['localhost']:
        print("This feature not yet implemented")
    else:
        command=("mysql -u" + dbset['DBUser'] + " -p" + dbset['DBPass'] + ' ' + dbset['DBName'] + " ")
        return(command)
    
def Log(cmd,e):
    return(loggerSetup.main(1,"CRITICAL",str(cmd)+' | ' + str(e)))

def Import(files):
    cmd = command+'< '+files+';'
    return(cmd)

def Export(files):
    cmd=command+'> '+files+';'
    return(cmd)
    
def AddEntry(table,references,values):
    cmd=command+' INSERT INTO {0} ({1}) VALUES ({2});'.format(str(table),str(references),str(values)
    return(cmd)

def DelEntry(table,references,values):
    cmd=command+' DELETE FROM {0} WHERE {1} = {2};'.format(str(table),str(references),str(values)
    return(cmd)
                                                             
def Run(cmd):
    import subprocess
    try:
        subprocess.check_call(cmd)
    except Exception as e:
        log(cmd,e)
                                                           
def main(inputs):
    import loggerSetup
    loggerSetup.main(1,'DEBUG','Init')
    ReadSettings()
    DBConnection()
    if '-h' in inputs:
        print('-h help file')
        print('-import database.sql')
        print('-export database.sql')
        print('-add Table,Column,Value')
        print('-delete Table,Row')
        print('Commands seperated by ; ')
        print('Examples:')
        print('-i /path/to/database.sql; -e database.sql; -add Individual,FName,John; -del Individual,John')
    elif '-i' in inputs:
        try:
            inputs = inputs.split(' ',1)[1]
            cmd = Import(inputs)
            print(cmd)
        except:
            pass
    elif '-e' in inputs:
        try:
            inputs = inputs.split(' ',1)[1]
            print('e')
        except:
            pass
    elif '-add' in inputs:
        inputs = ''
        return(inputs)
    elif '-del' in inputs:
        inputs = ''
        return(inputs)
    else:
        try:
            return(command + " " + inputs)
        except Exception as e:
            log(inputs,e)

if __name__ == "__main__":
    main(sys.argv[1])
