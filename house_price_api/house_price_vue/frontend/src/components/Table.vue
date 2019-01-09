<template>
  <div class="container">
    <b-table :data="isEmpty ? [] : postForm" :columns="columns" :bordered="true"
            :striped="true"
            :narrowed="true"
            :hoverable="true"
            :focusable="false"></b-table>
  </div>
</template>

<script>
/* eslint-disable */
import BTable from 'buefy/src/components/table/Table'
export default {
  components: {BTable},
  props: {
    postForm: {
        type: Object
    }
  },
  data () {
    const mock_data = [
      { 'id': 1, 'price': '162000', 'areaMeters': 45, 'rooms': 3, 'houseCondition': 'uusehitis',
        'buildYear': 2018, 'floor': 3, 'cityPart': 'Kadriorg',
        'houseMaterial': 'betoonmaja', 'energyClass': 'a', 'selectedHeating': 'elektriküte, maaküte, ahjuküte',
        'hasPool': '', 'hasSauna': 'hasSauna', 'hasBalcony': 'hasBalcony', 'hasTerrass': ''
      },

      { 'id': 2,'price': '35545466', 'areaMeters': 6665, 'rooms': 3, 'houseCondition': 'uusehitis',
        'buildYear': 2018, 'floor': 2, 'cityPart': 'Haabersti',
        'houseMaterial': 'puitmaja', 'energyClass': 'b', 'selectedHeating': 'elektriküte, maaküte, ahjuküte',
        'hasPool': 'hasPool', 'hasSauna': '', 'hasBalcony': '', 'hasTerrass': 'hasTerrass'
      },
    ]
    const columns = [{
                        field: 'id',
                        label: 'ID',
                        width: '40',
                        numeric: true
                    },
      {
                        field: 'price',
                        label: 'price',
                        width: '40',
                        numeric: true
                    },

                    {
                        field: 'areaMeters',
                        label: 'Area Meters',
                        numeric: true
                    },
                    {
                        field: 'rooms',
                        label: 'rooms',
                        width: '40',
                        numeric: true
                    },
                    {
                        field: 'houseCondition',
                        label: 'condition',

                    },
                    {
                        field: 'buildYear',
                        label: 'year',
                        numeric: true
                    },
                    {
                        field: 'floor',
                        label: 'floor',
                        numeric: true
                    },
                    {
                        field: 'cityPart',
                        label: 'cityPart',
                    },
                    {
                        field: 'houseMaterial',
                        label: 'material',
                    },
                    {
                        field: 'energyClass',
                        label: 'energy',
                    },
                    {
                        field: 'selectedHeating',
                        label: 'heating',
                    },
                    {
                        field: 'hasPool',
                        label: 'pool',
                    },
                    {
                        field: 'hasSauna',
                        label: 'sauna',
                    },
                    {
                        field: 'hasBalcony',
                        label: 'balcony',
                    },
                    {
                        field: 'hasTerrass',
                        label: 'terrass',
                    },

    ]

    return {
      columns,
      mock_data,
    }
  },
  name: 'Table',
  methods: {
  },
  mounted () {
    console.log(this.postForm)
  }
}
</script>

<style scoped>
  table#fixed { table-layout:fixed; }
  table#fixed td { overflow: hidden; }

</style>
