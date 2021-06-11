<template>
    <div id="input_box">
        <el-row class="demo-autocomplete">
        <el-col :span="12">
            <div class="sub-title">通过姓名检索首辅</div>
            <el-autocomplete
            class="inline-input"
            v-model="state1"
            :fetch-suggestions="querySearch"
            placeholder="请输入内容"
            @select="handleSelect"
            ></el-autocomplete>
        </el-col>
        </el-row>
    </div>
    <div id="info">
        <div id="my_radar">

        </div>
        <div id="intro">
            个人简介
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import * as d3 from 'd3';
import { RadarChart } from '../js/radarChart.js'
import axios from 'axios'

export default defineComponent({
    setup() {
        const primer_minister = ref([]);
        // 有关svg的数据
        /* 常量
        ---------------------------------------------------------------------------------------------------*/
        const margin = {top: 50, right: 200, bottom: 30, left: 100};
        const w_width = ref(window.innerWidth
            || document.documentElement.clientWidth
            || document.body.clientWidth);

        const w_height = ref(window.innerHeight
            || document.documentElement.clientHeight
            || document.body.clientHeight);

        const width = w_width*0.87 - margin.left - margin.right;
        const height = w_height*0.9 - margin.top - margin.bottom;

        const radarChartOptions = {
			w: 290,
			h: 350,
			margin: margin,
			maxValue: 20,
			levels: 6,
			roundStrokes: false,
			color: d3.scaleOrdinal().range(["#3366CC", "#FF9966"]),
			format: '.2f',
			legend: { title: '与平均值对比情况', translateX: 100, translateY: 40 },
			unit: ''
		};

        const querySearch = (queryString, cb) => {
            var results = queryString
                ? primer_minister.value.filter(createFilter(queryString))
                : primer_minister.value;
            // 调用 callback 返回建议列表的数据
            cb(results);
        };
        const createFilter = (queryString) => {
            return (primer_minister) => {
                return (
                primer_minister.value.toLowerCase().indexOf(queryString.toLowerCase()) ===
                0
                );
            };
        };
        const loadAll = () => {
            return [
                {value: '曹鼐'}, {value: '陈文'}, {value: '陈循'}, {value: '成基命'}, 
                {value: '范复粹'}, {value: '费宏'}, {value: '高拱'}, {value: '高榖'}, 
                {value: '顾秉谦'}, {value: '顾鼎臣'}, {value: '韩爌'}, {value: '胡广'}, 
                {value: '黄淮'}, {value: '黄立极'}, {value: '蒋德璟'}, {value: '蒋冕'}, 
                {value: '解缙'}, {value: '孔贞运'}, {value: '来宗道'}, {value: '李标'}, 
                {value: '李春芳'}, {value: '李东阳'}, {value: '李时'}, {value: '李廷机'}, 
                {value: '李贤'}, {value: '梁储'}, {value: '刘吉'}, {value: '刘健'}, 
                {value: '刘一燝'}, {value: '毛纪'}, {value: '彭时'}, {value: '商辂'}, 
                {value: '申时行'}, {value: '沈一贯'}, {value: '施凤来'}, {value: '万安'}, 
                {value: '王家屏'}, {value: '王锡爵'}, {value: '魏藻德'}, {value: '温体仁'}, 
                {value: '夏言'}, {value: '徐阶'}, {value: '徐溥'}, {value: '徐有贞'}, 
                {value: '许彬'}, {value: '严嵩'}, {value: '杨溥'}, {value: '杨荣'}, 
                {value: '杨士奇'}, {value: '杨廷和'}, {value: '杨一清'}, {value: '叶向高'}, 
                {value: '翟銮'}, {value: '张璁'}, {value: '张居正'}, {value: '张四维'}, 
                {value: '张至发'}, {value: '赵志皋'}, {value: '周延儒'}, {value: '朱赓'}, 
                {value: '朱国祯'},
            ];
        };
        const initRadarChart = () => {
            // 初始化信息
            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: 3.09},
						{axis: '首次上任年龄（5年）', value: 44/5},
						{axis: '享年（5年）', value: 48/5},
						//{axis: '出任首辅次数', value: 1}
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
						//{axis: '出任首辅次数', value: 1.33}
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        };
        const transRadarChart = (res) => {
            // 初始化信息
            let data = [
				{ name: '该首辅个人信息',
					axes: [
                        {axis: '任期总长（年）', value: res.scale},
						{axis: '首次上任年龄（5年）', value: res.begin_age/5},
						{axis: '享年（5年）', value: res.age/5},
						//{axis: '出任首辅次数', value: 1}
					]
				},
				{ name: '明代首辅平均值(61人)',
					axes: [
                        {axis: '任期总长（年）', value: 3.60},
						{axis: '首次上任年龄（5年）', value: 57.52/5},
						{axis: '享年（5年）', value: 70.16/5},
						//{axis: '出任首辅次数', value: 1.33}
					]
				}
			];

			let radar = RadarChart("#my_radar", data, radarChartOptions);
        }
        const handleSelect = (item) => {
            axios.get("http://localhost:5000/api/get_pm_info",{params:{name:item.value}})
                .then((res) => {
                    transRadarChart(res['data']['result']);
                });
        };
        onMounted(() => {
            primer_minister.value = loadAll();
            initRadarChart();
            });
            return {
            primer_minister,
            state1: ref(''),
            state2: ref(''),
            querySearch,
            createFilter,
            loadAll,
            initRadarChart,
            transRadarChart,
            handleSelect,
            };
    },
    data() {
        return {
            radar:null,
        }
    },
    mounted(){
    },
    methods:{
    }

})
</script>

<style>
@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");
</style>