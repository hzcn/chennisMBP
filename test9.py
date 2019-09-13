#just for commit
from itertools import combinations

ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


#for i in xs:
#    for j in xs:
#        for k in xs:
#            for l in xs:
#                SUM = i+j+k+l
#                if SUM <= 430:
#                    rs.append(SUM)
#print(max(rs))
def choose_best_sum(t, k, ls):
    sum2=0
    for dists in combinations(ls,k):
        sum1=sum(dists)
        if sum1>t:
            continue
        sum2=max(sum2,sum1)
    if sum2==0:
        return None
    return sum2


print(choose_best_sum(230,4,ls))
