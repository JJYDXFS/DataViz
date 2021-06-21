<template>
  <div id="graphic">
        <div id="sections">
            <section class="step">
                <div class="title " >Part1 大明首辅</div>
                自胡惟庸案后，朱元璋废除了丞相制度，亲自掌管六部<br/>
                而后朱棣建立了内阁制度，阁臣之首又称首辅，地位超然。
                作为皇帝的首席大秘，相比与他们所辅佐的帝王，首辅自身的故事却鲜有人关注<br/>
                本作品聚焦于展现掩藏在史书中关于首辅们的蛛丝马迹，希望能带给大家一些不一样的历史小知识
            </section>
            <section class="step">
                <div class="title" >Part2 历任首辅一览</div>
                我们依照清代张廷玉所编《明史·宰辅年表》整理了从黄淮到魏藻德在内的87任、共67位大明首辅<br/>
                右侧的散点图按时间顺序将每位首辅绘成一个点，同代的首辅颜色相同。将鼠标移入点内，可以查看首辅的姓名和上任时间<br/>
                从散点图中可以看出一个有趣的现象，首辅扎堆的年代总是多事之秋......
            </section>
            <section class="step">
                <div class="title" >Part3 首辅们从哪来？</div>
                跟首辅们打过初次照面后，让我们再来“查个户口”：明代的首辅都是哪的人呢？<br/>
                右侧的地图展现了自永乐朝始，首辅们的籍贯来源<br/>
                等动画加载完成后，移动到感兴趣的省份查看那里出身的首辅吧，或许还能找到几个老乡呢<br/>
                PS：这里就不得不提一下出了6位首辅的江西吉安府，既有主持编写了《永乐大典》的才子解缙，又有明代续航时间最长的首辅杨士奇
            </section>
            <section class="step">
                <div class="title" >Part4 “学霸”的世界</div>
                首辅作为明代文官之路的巅峰，是“学而优则仕”的最佳体现<br/>
                在明代，<a href="https://baike.baidu.com/item/%E7%A7%91%E4%B8%BE%E5%88%B6%E5%BA%A6/278041?fr=aladdin#1">科举制度</a>自下而上可大致分为乡试、会试、殿试三层。
                通过殿试的考生按名次被授予一甲/二甲/三甲出身。一甲只有三人，是人们熟知的状元/榜眼/探花，二甲进士和三甲同进士人数则较多，共有二三百人<br/>
                能成为首辅自然是优中选优，右侧的桑基图展现了历代首辅的学历分布。可以看出，状元不管在哪朝哪代都很吃香嘛<br/>
                唯一的那位布衣翰林也是我们的老熟人了：杨士奇
            </section>
            <section class="step">
                <div class="title" >Part5 盖棺定论</div>
                问汝平生功业，自有旁人说短长。谥号是古人死后，后人按其生平事迹给定的概括性评价。
                明代的首辅只要不出大差错，基本都能得到“文”这一美谥<a href="https://ctext.org/lost-book-of-zhou/shi-fa/zh">《逸周书·谥法解》</a><br/>
                “文正”是历代文人梦寐以求的谥号，明代首辅唯有李东阳得此殊荣。
                相传李东阳死前，好友杨一清前来探望，透露朝廷将给他文正的谥号。李东阳听罢竟起身在床上向杨磕了一个头
            </section>
            <section class="step">
                <div class="title" >Part6 党争之祸</div>
                <button class="switch-button" @click="showChessChart3d()">3D棋盘</button>
                <button class="switch-button" @click="showChessChart()">2D棋盘</button>
                <br/>
                东林党与阉党
            </section>
            <section class="step">
                <div class="title" >Part7 首辅详情</div>
                <InputWithSug/>
            </section>
            <section class="step">
                <div class="title" >Part 8 写在后面的话</div>
                暂时空白，等待最后填充一些参考资料
            </section>
        </div>
        <div id="vis">
            <transition mode="out-in">
                <component v-bind:is="comName" ref="myviz"></component>
            </transition>
        </div>
    </div>
  <footer style="text-align: center;">Copyright © 2021 章颖 傅苏知雨. All Rights Reserved</footer>
</template>

<script>
import {ref} from 'vue'

import {scroller} from '../src/js/scroller.js'
import Title from './components/Title.vue'
import Scatter from './components/Scatter.vue'
import HomeMap from './components/HomeMap.vue'
import OriginSankey from './components/OriginSankey.vue'
import CirclePacking from './components/CirclePacking.vue'
import RadarChart from './components/RadarChart.vue'
import ChessChart from './components/ChessChart.vue'
import ChessChart3d from './components/ChessChart3d.vue'
import Ending from './components/Ending.vue'

import InputWithSug from './components/InputWithSug.vue'

import * as d3 from 'd3';

var activateFunctions = [];
var updateFunctions = [];
var lastIndex = -1;
var activeIndex = 0;

export default {
  name: 'App',
  components: {
    Scatter,
    Title,
    HomeMap,
    OriginSankey,
    CirclePacking,
    ChessChart,
    ChessChart3d,
    RadarChart,
    InputWithSug,
    Ending,
  },
  data(){
    return{
        comName:"Title",
    };
  },
  mounted(){
      /**
       * 教程参考
       * https://vallandingham.me/scroller.html
       */
      this.initScroller();
      // 当活动section改变时，将调用不同的激活函数
      activateFunctions[0] = this.showTitle;
      activateFunctions[1] = this.showScatter;
      activateFunctions[2] = this.showHomeMap;
      activateFunctions[3] = this.showOriginSankey;
      activateFunctions[4] = this.showCirclePacking;
      activateFunctions[5] = this.showChessChart3d;
      activateFunctions[6] = this.showRadarChart;
      activateFunctions[7] = this.showEnding;
  },
  methods:{
      initScroller(){
        var comp = this;
        var scroll = scroller()
            .container(d3.select("#graphic"));
        // 逐步调用
        scroll(d3.selectAll('.step'));
            
        // 设置事件句柄
        scroll.on('active', function (index){
            // 高亮当前section
            d3.selectAll('.step')
            .style('opacity', function (d, i) { return i === index ? 1 : 0.1; });
                
            comp.activateViz(index);
        });
      },

      /**
       * 激活对应的数据可视化图表
       * @param index - 激活部分的下标
      */
      activateViz(index) {
          activeIndex = index;
          var sign = (activeIndex - lastIndex) < 0 ? -1 : 1;
          var scrolledSections = d3.range(lastIndex + sign, activeIndex + sign, sign);
          scrolledSections.forEach(function (i) {
              activateFunctions[i]();
            });
              
        lastIndex = activeIndex;
      },
      showTitle(){
          this.comName = "Title";
      },
      showScatter(){
          this.comName = "Scatter";
      },
      showHomeMap(){
          this.comName = "HomeMap";
      },
      showOriginSankey(){
          this.comName = "OriginSankey";
      },
      showCirclePacking(){
          this.comName = "CirclePacking";
      },
      showChessChart(){
          this.comName = "ChessChart";
      },
      showChessChart3d(){
          this.comName = "ChessChart3d";
      },
      showRadarChart(){
          this.comName = "RadarChart";
      },
      showEnding(){
          this.comName = "Ending";
      },
  }
}
</script>

<style>
#sections{
    position: relative;
    display: inline-block;
    width: 17%;
    top: 0px;
    z-index: 90;
    margin-left: 5%;
    font-size: 18px;
    padding-bottom: 230px;
}

.step{
    margin-bottom: 200px;
    font-size: 18px;
}

.title{
    font-size: large;
    font-family: Arial, Helvetica, sans-serif;
}

.switch-button{
    background-color: #4f9ed3;
    border: none;
    border-radius: 6px;
    color: white;
    padding: 10px 25px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    margin: 4px 2px;
    cursor: pointer;
}

#vis{
    display: inline-block;
    position: fixed;
    top: 40px;
    z-index: 1;
    margin-left: 2%;

    height: 600px;
    width: 70%;
    /* background-color: #ddd; */
}
/* 组件过渡样式
 * https://blog.csdn.net/weixin_42218847/article/details/81481782
 */
.v-enter,.v-leave-to{
    opacity: 0;
    transform: translateX(150px);
}
        
.v-enter-active,.v-leave-active{
    transition: all 0.5s ease;
}
</style>
