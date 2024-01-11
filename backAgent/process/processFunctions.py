from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Lock

def runProc(agents, simulationConditions, nbProc = 3):

    # Queues inits
    queueIN = Queue()
    queueOUT = Queue()
    lock = Lock()

    #Process list
    process = []
    for i in range(nbProc):
        process.append( 
            Process(target=runAgent, args=(lock, queueIN, queueOUT, simulationConditions)) 
        )

    # Agents are added to queue
    for a in agents :
        queueIN.put(a)

    # Starting process
    for proc in process :
        proc.start()
    
    # Joining
    for proc in process :
        proc.join()

    # retuning results
    results = []
    while not queueOUT.empty() :
        results.append( queueOUT.get(timeout=10) )

    return(results)


def runAgent(lock, queueIN, queueOUT, simulationConditions):

    #Making sure the queue is not empty
    lock.acquire()
    while not queueIN.empty() :
        agent = queueIN.get(timeout=10) 
        lock.release()

        # Training the agent
        res = agent.train(simulationConditions)

        # Return results of training
        queueOUT.put(res)
        lock.acquire()
    lock.release()