
function collectData(){
    var range = document.getElementById("range").value
    eel.write("sadf")
    eel.frameLoop(range)
    
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