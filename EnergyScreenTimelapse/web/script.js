
function collectData(){
    var range = document.getElementById("range").value
    eel.frameLoop(range)
    alert('The timelapse has started recording')
}
function stop(){
    eel.stop()
    window.close()
}
function updateMonitor(val){
    document.getElementById("monitor").innerHTML = val
}
function select(){
    eel.selectFolder();
}
eel.expose(writePath)
function writePath(path){
    document.getElementById("pathview").innerHTML = path
}