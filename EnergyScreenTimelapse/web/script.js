
function collectData(){
    var range = document.getElementById("range").value
    var lapsName = document.getElementById("filename").value

    eel.frameLoop(range, lapsName)
    
}
function stop(){
    eel.stop()
    window.close()
}
function updateMonitor(val){
    document.getElementById("monitor").innerHTML = val
}
