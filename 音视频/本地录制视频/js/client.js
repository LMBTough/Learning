var videoplay = document.querySelector('video#player');
var stream_all
function gotMediaStream(stream){
        videoplay.srcObject = stream;
        stream_all = stream
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



var buffer;

// 当该函数被触发后，将数据压入到 blob 中
function handleDataAvailable(e){
        if(e && e.data && e.data.size > 0){
                buffer.push(e.data);
        }
}

var startButton = document.querySelector('button#record');
function startRecord(){
        buffer = [];
        // 设置录制下来的多媒体格式 
        var options = {
                mimeType: 'video/webm;codecs=vp8'
        }
        console.log(1);
        // 判断浏览器是否支持录制
        if(!MediaRecorder.isTypeSupported(options.mimeType)){
                console.error(`${options.mimeType} is not supported!`);
                return;
        }

        try{
                // 创建录制对象
                mediaRecorder = new MediaRecorder(stream_all, options);
        }catch(e){
                console.error('Failed to create MediaRecorder:', e);
                return;
        }

        // 当有音视频数据来了之后触发该事件
        mediaRecorder.ondataavailable = handleDataAvailable;
        // 开始录制
        mediaRecorder.start(10);

}
startButton.onclick = startRecord

var recplayButton = document.querySelector('button#recplay')
recplayButton.onclick = function(){
     var blob = new Blob(buffer, {type: 'video/webm'});
     recvideo.src = window.URL.createObjectURL(blob);
     recvideo.srcObject = null;
     recvideo.controls = true;
     recvideo.play();
} 
var btnDownload = document.querySelector('button#download')
btnDownload.onclick = ()=> {
        var blob = new Blob(buffer, {type: 'video/webm'});
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');

        a.href = url;
        a.style.display = 'none';
        a.download = 'aaa.webm';
        a.click();
}
