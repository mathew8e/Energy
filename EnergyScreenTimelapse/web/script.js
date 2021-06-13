
function collectData(){
    var range = document.getElementById("range")
    var lapsName = document.getElementById("filename")

    eel.start(range, range, lapsName)
}
function stop(){
    eel.stop()
    window.close()
}
function updateMonitor(val){
    document.getElementById("monitor").innerHTML = val
}