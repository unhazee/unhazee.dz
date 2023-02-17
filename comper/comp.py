if __name__ == '__main__' :
    with open("dfg.txt", mode='r', encoding='utf-8') as f:
        lst = f.readlines()
    my_list = [elem.strip()[elem.find('a'):].capitalize() if "a" in elem else '' for elem in lst]
    print(f"\nВихідний список: {my_list}")