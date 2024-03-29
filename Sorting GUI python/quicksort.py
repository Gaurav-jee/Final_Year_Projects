import time
def partition(data,head,tail,drawData,timeTick):
    border = head
    pivot =data[tail]

    drawData(data, getColorArray(len(data), head, tail, border,border))
    time.sleep(timeTick)

    for j in range(head,tail):
        if data[j] < pivot:
            
            drawData(data, getColorArray(len(data), head, tail, border,j,True))
            time.sleep(timeTick)

            data[border],data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border,j))
        time.sleep(timeTick)

    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border,tail,True))
    time.sleep(timeTick)
    
    data[border],data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head,tail, drawData,timeTick):
    if head < tail:
        partitionIdx = partition(data, head,tail,drawData, timeTick)

        #LEFT pARTITION
        quick_sort(data,head, partitionIdx -1 , drawData, timeTick)

        #Right partition
        quick_sort(data,partitionIdx +1 ,tail, drawData, timeTick)


def getColorArray(datalen,head , tail, border,currIdx,isSwapping =False):  
    ColorArray = []
    for i in range(datalen):
        #basecoloring
        if i >= head and i <= tail:
            ColorArray.append('grey')
        else :
            ColorArray.append('white')

        if i == tail:
            ColorArray[i] = 'blue'
        elif i == border :
            ColorArray[i] = 'red'
        elif i == currIdx:
            ColorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currIdx:
                ColorArray[i] = 'green'

    return ColorArray