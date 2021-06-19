<template>

    <div id="canvas-frame"></div>

</template>

<script>
import { defineComponent } from "vue";
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
// import { objectSelection } from '../js/objSelection.js';
import * as d3 from 'd3';

export default defineComponent({
  data() {
    return {}
  },
  mounted(){
    var chess=this;
    d3.json("./data/chess.json").then(function(data) {
        chess.drawChessChart(data);
    });
  },

  methods:{
    drawChessChart(data) {
        // 有关canvas尺寸的数据
        /* 常量
        ---------------------------------------------------------------------------------------------------*/
        var width = window.innerWidth
        || document.documentElement.clientWidth
        || document.body.clientWidth;

        var height = window.innerHeight
        || document.documentElement.clientHeight
        || document.body.clientHeight;
        // 边距
        var margin = {top: 10, right: 100, bottom: 60, left: 150};
        var canWidth = width*0.87 - margin.left - margin.right;
        var canHeight = height*0.9 - margin.top - margin.bottom;

        // 初始化div/scene/camera/renderer
        var threeDiv = document.getElementById('canvas-frame');
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(50, canWidth/canHeight, 0.1, 1000);

        var renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
        // 设置renderer属性
        renderer.setClearColor( 0xffffff, 0 );  // 白色背景
        renderer.setSize(canWidth, canHeight);
        // 把renderer加入页面
        threeDiv.appendChild(renderer.domElement);
        // 加载材质的函数
        var getTexture = function(str){
            var loader = new THREE.TextureLoader();
            return loader.load(str);
        }
        // 绘制立体图形
        // 棋盘
        var geometry = new THREE.BoxGeometry(450,10,400);

        var material = new THREE.MeshLambertMaterial({
            color: 0xffffff,
            map: getTexture('img/chess_bg.png'),
            wireframe: false
        });

        var cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // 棋子

        var chess = new Array();
        var chess_material = new Array();
        var r_chess = new Array();

        for (let i = 0; i < data.length; i++) { 
            chess[i] = new THREE.CylinderGeometry(20, 20, 10, 25);

            chess_material[i] = new THREE.MeshBasicMaterial({
                color: 0xffffff,
                map: getTexture('img/'+data[i].name+'.jpg'),
                wireframe: false
            });

            r_chess[i] = new THREE.Mesh(chess[i], chess_material[i]);
            if(data[i].pos_x<5){
                r_chess[i].position.set(data[i].pos_x*45-190,10,data[i].pos_y*45-180);
            }
            else{
                r_chess[i].position.set(data[i].pos_x*45-215,10,data[i].pos_y*45-180);
            }

            scene.add(r_chess[i]);
        }

        // 打光
        var ambient = new THREE.AmbientLight(0x444444);
		scene.add(ambient);

        // 控制器
        var controls = new OrbitControls(camera, renderer.domElement);
        controls.target = cube.position; // 控制焦点
        controls.autoRotate = true;   // 自动旋转
        controls.enableZoom = true;
        scene.controls = controls;
        // 设置相机视角
        camera.position.set( 250, 120, 250 );

        // 参考平面
        var initGrid = function() {
            var gridXZ = new THREE.GridHelper(500, 10, 0xa23131, 0xa23131);//4个参数分别是：网格宽度、等分数、中心线颜色，网格线颜色
            gridXZ.position.set(25,0,50);
            gridXZ.material.linewidth = 10;
            scene.add(gridXZ);
        }
        // 渲染函数
        var render = function (){
            // 使用控制器
            scene.controls.update();
            renderer.render(scene, camera);
            requestAnimationFrame(render);
        }
        // initGrid();
        render();

    }
  }

})
</script>

<style>
div.chess_tooltip {	
    position: absolute;			
    text-align: center;			
    width: 180px;					
    height: 60px;					
    padding: 2px;				
    font: 14px sans-serif;
    font-weight: bold;
    line-height: 20px;	
    border: 0px;	
    border-radius: 8px;			
    pointer-events: none;
    text-shadow: #fff 0.8px 0 0, #fff 0 0.8px 0, #fff -0.8px 0 0, #fff 0 -0.8px 0;	
}

#canvas-frame {
    position:absolute;
}

#interaction{
    position:absolute;
    left:80vw;
    top:5vh;
    width: 20vw;
    height: 20vh;
    z-index: 10;
	font-size: 30px;
}
</style>