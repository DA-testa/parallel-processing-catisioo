# python3

def parallel_processing(n, m, data):
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    output = []
    thread_number = [0]*n

    for i in range (m):
        nextt = thread_number.index(min(thread_number))

        beginning = thread_number[nextt]
        
        end = beginning + data[i]

        thread_number[nextt] = end

        output.append((nextt, beginning))


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()
