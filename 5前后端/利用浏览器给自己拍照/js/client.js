'use strict'

// 获取 HTML 页面中的 video 标签  
var videoplay = document.querySelector('video#player');

// 播放视频流
function gotMediaStream(stream){
        videoplay.srcObject = stream;
}

function handleError(err){
        console.log('getUserMedia error:', err);
}

// 对采集的数据做一些限制
var constraints = {
                        video : {
                                width: 1280,
                                height: 720,
                                frameRate:15,
                        },
                        audio : false
                   }

// 采集音视频数据流
navigator.mediaDevices.getUserMedia(constraints)
                        .then(gotMediaStream)
                        .catch(handleError);


var picture = document.querySelector('canvas#picture');
picture.width = 640;
picture.height = 480; 

document.querySelector("button#TakePhoto").onclick = function (){
    picture.getContext('2d').drawImage(videoplay, 0, 0, picture.width, picture.height);
}

function downLoad(url){
    var oA = document.createElement("a");
    oA.download = 'photo';// 设置下载的文件名，默认是'下载'
    oA.href = url;
    document.body.appendChild(oA);
    oA.click();
    oA.remove(); // 下载之后把创建的元素删除
}

document.querySelector("button#save").onclick = function (){
    downLoad(picture.toDataURL("image/jpeg"));
    // console.log(picture.toDataURL("image/jpeg"))
}

var filtersSelect = document.querySelector("select#filter")
filtersSelect.onchange = function(){
    console.log('1');
    picture.className = filtersSelect.value;
    
}

