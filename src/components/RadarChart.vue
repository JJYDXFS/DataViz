<template>
    <div id="info">
        <div id="my_radar">

        </div>
        <div id="intro">
            <h2 style="text-align:center;"> {{detail.name}} </h2>
            <p class="detail center">出任首辅{{detail.times}}次</p>
            <p class="detail center">任期总时长{{detail.scale}}年</p>
            <p class="detail info">
                {{detail.info}}
            </p>
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import * as d3 from 'd3';
import { RadarChart } from '../js/radarChart.js'

export default defineComponent({
    setup() {
        // 有关svg的数据
        /* 常量
        ---------------------------------------------------------------------------------------------------*/
        const margin = {top: 100, right: 200, bottom: 30, left: 100};
        const w_width = ref(window.innerWidth
            || document.documentElement.clientWidth
            || document.body.clientWidth);

        const w_height = ref(window.innerHeight
            || document.documentElement.clientHeight
            || document.body.clientHeight);

        const width = w_width*0.87 - margin.left - margin.right;
        const height = w_height*0.9 - margin.top - margin.bottom;

        var detail = ref({
                name: "曹鼐",
                scale: 3.09,
                begin_age: 44,
                age: 48,
                times: 1,
                info: "曹鼐（1402年－1449年9月1日），字万钟，号恒山。北直隶宁晋（今河北宁晋）人。明朝初年名臣。曹鼐自少为人豪爽，有大志，博览群书。宣德元年（1426年），中乡试第二，任代州训导，改派江西泰和县典史。明宣宗宣德八年（1433年）成癸丑科一甲第一名进士（状元），初授翰林院修撰。正统元年（1436年），充经筵讲官。正统五年（1440年），因杨荣、杨士奇举荐，进入文渊阁，参预机务。于正统十二年至正统十四年间（1447年－1449年）为内阁首辅，累官至吏部左侍郎兼翰林学士。正统十四年（1449年），曹鼐随英宗亲征，于土木之变中殉难。明代宗继位后，追赠荣禄大夫、少傅、吏部尚书兼文渊阁大学士，谥号“文襄”。英宗复位，加赠太傅，改谥“文忠”。"
        });

        const radarChartOptions = {
			w: 290,
			h: 350,
			margin: margin,
			maxValue: 20,
			levels: 6,
			roundStrokes: false,
			color: d3.scaleOrdinal().range(["#3366CC", "#FF9966"]),
			format: '.2f',
			legend: { title: '与平均值对比情况', translateX: 150, translateY: 43 },
			unit: ''
		};
        const initRadarChart = () => {
            // 初始化信息，默认为姓名拼音序第一位-曹鼐
            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: 3.09},
						{axis: '首次上任年龄（5年）', value: 44/5},
						{axis: '享年（5年）', value: 48/5},
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        };
        const transRadarChart = (res) => {
            // 初始化信息
            detail.value=res;

            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: res.scale},
						{axis: '首次上任年龄（5年）', value: res.begin_age/5},
						{axis: '享年（5年）', value: res.age/5},
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        }
        onMounted(() => {
            initRadarChart();
            });
            return {
            initRadarChart,
            transRadarChart,
            detail,
        };
    },
    data() {
        return {
            //radar:null,
        }
    },

})
</script>

<style>
@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");

#my_radar {
    float: left;
}

#intro {
    float: left;
    width: 35%;
}

.detail{
    font-size: 16px;
}

.info{
    font-size: 14px;
}

.center{
    text-align: center;
}
</style>