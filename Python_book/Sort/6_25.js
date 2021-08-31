//실패율
function solution(N, stages) {
    let stage = stages.sort();
    let sum_list = []
    let count_t = []
    // console.log("stage : ", stage)
    for(var t = 1 ; t <= N; t++){
        var temp = 0
        stage.map((a) => {
            if(a >= t){
                temp++
            }
        })
        sum_list[t - 1] = temp
    }
    // console.log("sum_list : ", sum_list)
    for(var t = 1 ; t <= N; t++){
        var temp = 0
        stage.map((item) => {
            if(item == t){
                temp++
            }
        })
        count_t.push(temp)
    }
    var answer_temp = {}
    for(var t = 0 ; t <= N - 1; t++){
        var num = count_t[t] / sum_list[t]
        answer_temp[parseInt(t+1)] = num
    }
    // console.log(answer_temp)
    var keysSorted = 0
    keysSorted = Object.keys(answer_temp).sort(function(a,b){return answer_temp[b] - answer_temp[a]})
    keysSorted.forEach((item, i) => {
        keysSorted[i] = parseInt(item)
    })
    console.log(keysSorted)
    return keysSorted;
}

//Python
