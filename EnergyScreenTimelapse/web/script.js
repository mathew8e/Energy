
function collectData(){
    var range = document.getElementById("range").value
    var lapsName = document.getElementById("filename").value
    eel.start(lapsName) 

    eel.asyncfunc(range)
    
}
function stop(){
    eel.stop()
    window.close()
}
function updateMonitor(val){
    document.getElementById("monitor").innerHTML = val
}
