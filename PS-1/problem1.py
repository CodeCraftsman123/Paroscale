from threading import Thread, Lock
class FileWork:
    @staticmethod
    def open_file_and_read():
        file_obj = open("problem1_file2.txt","r")
        file_content=list()

        while True:
            line = file_obj.readline()
            if not line:
                break
            else:
                file_content.append(line)

        i=0
        while(i<len(file_content)):
            if(file_content[i] == "--\n"):
                file_content.pop(i)
            i+=1

        return file_content

class ThreadWork:
    global_unique_set=set()
    lock=Lock()

    @staticmethod
    def find_unique(current_section):
        for element in current_section:
            with ThreadWork.lock:
                ThreadWork.global_unique_set.add(element)
    
        
    @staticmethod
    def clean_content(file_content):
        file_content=file_content.strip().split()
        i=0
        while i < len(file_content):
            file_content[i]=int(file_content[i])
            i+=1
        ThreadWork.find_unique(file_content)
    
    @staticmethod
    def print_list():
        global_unique_list=list(ThreadWork.global_unique_set)
        print(f"Unique elements:{global_unique_list}")


    @staticmethod
    def create_and_run_threads(file_content):
        threads = list()
        i=0
        while(i<len(file_content)):
            t=Thread(target=ThreadWork.clean_content,args=[file_content[i]])
            threads.append(t)
            i+=1

        i=0
        while(i < len(file_content)):
            threads[i].start()
            i+=1

        i=0 
        while(i < len(file_content)):
            threads[i].join()
            i+=1

    



if __name__ == "__main__":
    file_content=FileWork.open_file_and_read()
    ThreadWork.create_and_run_threads(file_content)
    ThreadWork.print_list()
