<template>
  <div id="graphic">
        <div id="sections">
            <section class="step">
                <div class="title " >Part1 大明首辅</div>
                自胡惟庸案后，朱元璋废除了丞相制度，亲自掌管六部<br/>
                待到永乐年间，朱棣建立内阁作为皇帝的咨政机构。阁臣之首又称首辅，地位超然。
                作为皇帝的首席大秘，相比于他们所辅佐的帝王，首辅自身的故事却鲜有人关注<br/>
                本作品聚焦于展现掩藏在史书中关于首辅们的蛛丝马迹，希望能带给大家一些不一样的历史小知识
            </section>
            <section class="step">
                <div class="title" >Part2 历任首辅一览</div>
                我们依照清代张廷玉所编
                <a href="https://baike.baidu.com/reference/1080773/6711rzSlvDTwa92ek81yVUJZsicKrw3IZPQ2JgH_3_jbyT4A9gfaYurn9RmjrqHP1_ONFgsY8ZunIzsvZ_Xv8WcVxNfsstCq7WG3aDUA" target="_blank" >
                《明史·宰辅年表》</a>
                整理了从黄淮到魏藻德在内的87任、共67位大明首辅<br/>
                右侧的散点图按时间顺序将每位首辅绘成一个点，同代的首辅颜色相同。将鼠标移入点内，可以查看首辅的姓名和上任时间<br/>
                从散点图中可以看出一个有趣的现象，首辅扎堆的年代总是多事之秋......
            </section>
            <section class="step">
                <div class="title" >Part3 首辅们从哪来？</div>
                跟首辅们打过初次照面后，让我们再来“查个户口”：明代的首辅都是哪的人呢？<br/>
                右侧的地图展现了自永乐朝始，首辅们的籍贯来源<br/>
                等动画加载完成后，移动到感兴趣的省份查看那里出身的首辅吧，或许你还能找到几个老乡呢<br/>
                PS：这里就不得不提到连出了6位首辅大人的江西吉安府，既有主持编写了《永乐大典》的才子解缙，又有明代续航时间最长的首辅杨士奇
            </section>
            <section class="step">
                <div class="title" >Part4 “学霸”的世界</div>
                首辅作为明代文官之路的巅峰，是“学而优则仕”的最佳体现<br/>
                在明代，<a href="https://baike.baidu.com/item/%E7%A7%91%E4%B8%BE%E5%88%B6%E5%BA%A6/278041?fr=aladdin#1" target="_blank" >科举制度</a>自下而上可大致分为乡试、会试、殿试三层。
                通过殿试的考生按名次被授予一甲、二甲、三甲出身<br/>
                一甲只有三人，是人们熟知的状元/榜眼/探花。二甲进士和三甲同进士人数则较多，共有二三百人<br/>
                能成为首辅自然是优中选优，右侧的桑基图展现了历代首辅的学历分布。可以看出，状元不管在哪朝哪代都很吃香<br/>
                唯一的那位布衣翰林也是我们的老熟人了：杨士奇杨阁老
            </section>
            <section class="step">
                <div class="title" >Part5 盖棺定论</div>
                问汝平生功业，自有旁人说短长。谥号是古人死后，后人按其生平事迹给定的概括性评价<br/>
                明代的首辅只要不出大差错，基本都能得到“文”这一美谥<a href="https://ctext.org/lost-book-of-zhou/shi-fa/zh" target="_blank" >&nbsp;详见《逸周书·谥法解》</a><br/>
                “文正”是历代文人梦寐以求的谥号，明代首辅唯有李东阳得此殊荣。
                相传李东阳死前，好友杨一清前来探望，并告知他朝廷将授予他“文正”的谥号。李东阳听罢竟起身在床上向杨磕了一个头
            </section>
            <section class="step">
                <div class="title" >Part6 党争之祸</div>
                明朝中后期朝堂各党派之间争权夺利、纷争不断。党争失衡可以说是加速明朝灭亡的动因之一。其中以明末东林党与阉党之争尤甚<br/>
                万历天启年间，两党首辅轮番上任把持朝政。右侧棋盘图在楚河汉界两侧分别放置了两党的代表人物。切换2D棋盘，可以交互查看每颗棋子对应的人物介绍（红色为东林党，黑色为阉党）<br/>
                <button class="switch-button" @click="showChessChart3d()">3D棋盘</button>
                <button class="switch-button" @click="showChessChart()">2D棋盘</button>
                <br/>
                彼时阉党人士还仿照《水浒传》编写了
                <a href="https://baike.baidu.com/item/%E4%B8%9C%E6%9E%97%E7%82%B9%E5%B0%86%E5%BD%95" target="_blank">《东林党点将录》</a>
                ，颇可玩味
            </section>
            <section class="step">
                <div class="title" >Part7 首辅详情</div>
                行至此处，本作品的主要内容已基本结束。让我们再来回顾一下这些大明首辅。
                试试在下面的输入框中通过姓名检索首辅生平吧(仅含生卒年可考的61位大人)
                <InputWithSug/>
                右侧的雷达图给出了该首辅个人信息和平均值的对比情况。你选中的首辅跑赢平均值了吗？<br/>
                在计算均值时，我们惊讶地发现首辅们的平均寿命年逾古稀，而大明皇帝的平均寿命则只有42...
            </section>
            <section class="step">
                <div class="title" >Part 8 写在后面的话</div>
                短短几页划过，于创作者而言真是漫长的旅程。从开始收集数据时遍寻古籍细细考据，
                到抉择适当图表以展现内容时苦思冥想，再到编码选色Debug......个中滋味，唯有自知<br/>
                所幸最后还是能呈现出最初设想的效果。也希望这个作品可以给更多历史爱好者带去一些乐趣，
                给对这段历史不甚了解的观众带去一些掌故趣闻<br/>
                受篇幅所限，我们整理过程中发现的许多有趣细节无法展开：例如崇祯朝多用三甲出身的首辅，其中三人同为万历四十七年同进士；
                四朝元老杨士奇的真正死因恐是被不孝子气死等等......就留待善于发现的你去从数据中揭秘吧！
            </section>
        </div>
        <div id="vis">
            <transition mode="out-in">
                <component v-bind:is="comName" ref="myviz"></component>
            </transition>
        </div>
    </div>
   <footer style="text-align: center;">
   Copyright © 2021-2022 JJYDXFS × 复苏. All Rights Reserved
   </footer>
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
    width: 18%;
    top: 0px;
    z-index: 90;
    margin-left: 4%;
    font-size: 18px;
    padding-bottom: 60px;
}

.step{
    margin-bottom: 60px;
    font-size: 18px;
}

.title{
    font-size: large;
    font-family: Arial, Helvetica, sans-serif;
    padding-bottom: 10px;
}

.switch-button{
    background-color: #4298d1b0;
    border: none;
    border-radius: 6px;
    color: white;
    padding: 10px 25px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    margin: 4px 8px;
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

a:link{ /* 指正常的未被访问过的链接*/
    text-decoration:none;
    color:#697e93;
}  

a:visited{ /*指已经访问过的链接*/
    text-decoration:none;
    color:#697e93; 
}

a:hover{ /*指鼠标在链接*/
    text-decoration:none;
    color:#013a73;
}

a:active{ /* 指正在点的链接*/ 
    text-decoration:none;
    color:#697e93;
}
</style>
