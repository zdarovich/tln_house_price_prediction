<template>
<div class="container">
    <table class="table" id="fixed">
      <col width="100px" />
      <col width="1000px" />
      <thead>
          <tr>
            <th>Area meters (m^2)</th>
            <td>
              <div class="tile is-parent">
                <article class="tile is-child">
                  <article class="tile is-child is-3">
                    <b-input placeholder="Area meters"
                              v-model="areaMeters"
                              type="number"
                              min="0"
                              max="99">
                    </b-input>
                  </article>
                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="areaMeters > 0 && areaMeters < 9999">{{areaMeters}}</b-tag>
                </article>
              </div>
            </td>
          </tr>
          <tr>
            <th>Rooms</th>
                        <td>
              <div class="tile is-parent">
                <article class="tile is-child">
                  <article class="tile is-child is-2">
                    <b-input placeholder="Rooms"
                              v-model="rooms"
                              type="number"
                              min="0"
                              max="99">
                    </b-input>
                  </article>
                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="rooms > 0 && rooms < 100">{{rooms}}</b-tag>
                </article>
              </div>
            </td>

          </tr>
          <tr><th>Build Year</th>
                      <td>
              <div class="tile is-parent">
                <article class="tile is-child">
                  <article class="tile is-child is-2">
                    <b-input placeholder="Build year"
                              v-model="buildYear"
                              type="number"
                              min="1700"
                              max="2019">
                    </b-input>
                  </article>
                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="buildYear > 1699 && buildYear < 2020">{{buildYear}}</b-tag>
                </article>
              </div>
            </td>
</tr>
          <tr><th>Floor</th>
            <td>
              <div class="tile is-parent">
                <article class="tile is-child">
                  <article class="tile is-child is-2">
                    <b-input placeholder="Floor"
                              v-model="floor"
                              type="number"
                              min="0"
                              max="99">
                    </b-input>
                  </article>
                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" size="is-small" v-if="floor > 0 && floor < 100">{{floor}}</b-tag>
                </article>
              </div>
            </td>
</tr>
          <tr><th>Condition</th>
                      <td><div class="tile is-parent">
                <article class="tile is-child">
                  <b-select v-model="houseCondition" placeholder="Choose house condition">
                        <option value=0>Choose house condition</option>
                        <option value=1>uusehitis</option>
                        <option value=2>renoveeritud</option>
                        <option value=3>remonti vajav</option>
                </b-select>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="houseCondition != 0">{{conditionMapping()}}</b-tag>
                </article>
              </div></td>
</tr>
          <tr><th>City Part</th>            <td><div class="tile is-parent">
                <article class="tile is-child">
                  <b-select v-model="cityPart" placeholder="Choose city part">
                        <option value="">Choose city part</option>
                        <option value="Haabersti">Haabersti</option>
                        <option value="Kadriorg">Kadriorg</option>
                        <option value="Kesklinn">Kesklinn</option>
                        <option value="Kristiine">Kristiine</option>
                        <option value="Lasnamäe">Lasnamäe</option>
                        <option value="Mustamäe">Mustamäe</option>
                        <option value="Nõmme">Nõmme</option>
                        <option value="Pirita">Pirita</option>
                        <option value="Põhja-Tallinn">Põhja-Tallinn</option>
                        <option value="Vanalinn">Vanalinn</option>
                </b-select>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="cityPart.length > 0">{{cityPart}}</b-tag>
                </article>
              </div></td>
</tr>
          <tr><th>House material</th>
            <td>
          <div class="tile is-parent">
                <article class="tile is-child">
                  <b-select v-model="houseMaterial" placeholder="Choose house material">
                        <option value="">Choose house material</option>
                        <option value="betoonmaja">Betoonmaja</option>
                        <option value="paneelmaja">Paneelmaja</option>
                        <option value="kivimaja">Kivimaja</option>
                        <option value="palkmaja">Palkmaja</option>
                        <option value="plokkmaja">Plokkmaja</option>
                        <option value="palk-kivimaja">Palk-kivimaja</option>
                        <option value="puitmaja">Puitmaja</option>
                </b-select>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="houseMaterial.length > 0">{{houseMaterial}}</b-tag>
                </article>
              </div>
          </td>
</tr>
          <tr><th>Energy Class</th>            <td>
          <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-select v-model="energyClass" placeholder="Choose energy class">
                        <option value="">Choose energy class</option>
                        <option value="a">A</option>
                        <option value="b">B</option>
                        <option value="c">C</option>
                        <option value="d">D</option>
                        <option value="e">E</option>
                        <option value="f">F</option>
                        <option value="g">G</option>
                  </b-select>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="energyClass.length > 0">{{energyClass}}</b-tag>
                </article>
              </div>
          </td>
</tr>
          <tr><th>Heating</th>            <td>
            <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-select multiple native-size="8" v-model="selectedHeating" placeholder="Choose heating">
                        <option value="elektriküte">elektriküte</option>
                        <option value="gaasiküte">gaasiküte</option>
                        <option value="ahjuküte">ahjuküte</option>
                        <option value="maaküte">maaküte</option>
                        <option value="autnoomne küte">autnoomne küte</option>
                        <option value="tahkekütus">tahkekütus</option>
                        <option value="keskküte">keskküte</option>
                        <option value="õhksoojuspump">õhksoojuspump</option>
                        <option value="kamin">kamin</option>
                        <option value="põrandaküte">põrandaküte</option>
                        <option value="kombineeritud küte">kombineeritud küte</option>
                  </b-select>

                </article>
                <article class="tile is-child">
                  <b-taglist v-for="heating in selectedHeating" :key="heating">
                    <b-tag type="is-primary">{{heating}}</b-tag>
                   </b-taglist>
                </article>
              </div>
</td>
</tr>
          <tr><th>Terrass</th>            <td>
            <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-switch v-model="hasTerrass"
                      true-value="1"
                      false-value="0">
                  </b-switch>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="hasTerrass == 1">Has terrass</b-tag>
                </article>
              </div>
            </td>
</tr>
          <tr><th>Balcony</th>            <td> <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-switch v-model="hasBalcony"
                      true-value="1"
                      false-value="0">
                  </b-switch>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="hasBalcony == 1">Has balcony</b-tag>
                </article>
              </div></td>
</tr>
          <tr><th>Sauna</th>            <td> <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-switch v-model="hasSauna"
                      true-value="1"
                      false-value="0">
                  </b-switch>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="hasSauna == 1">Has sauna</b-tag>
                </article>
              </div></td>
</tr>
          <tr><th>Pool</th>                        <td> <div class="tile is-parent">
                <article class="tile is-child ">
                  <b-switch v-model="hasPool"
                      true-value="1"
                      false-value="0">
                  </b-switch>

                </article>
                <article class="tile is-child">
                      <b-tag type="is-primary" v-if="hasPool == 1">Has pool</b-tag>
                </article>
              </div></td>
</tr>
      </thead>
    </table>
      <div class="section">
        <h1>{{predicted_price}}</h1>
      </div>
    <div class="section">
      <a class="button is-primary is-large" @click="getPredictionFromBackend">Predict</a>
    <a class="button is-light is-large">Reset</a>
    </div>
      <Table :postForm="data"></Table>
      <VueChartJS :postForm="data"></VueChartJS>
  </div>
</template>

<script>
import axios from 'axios'
import Table from './Table'
import VueChartJS from './VueChartJS'
var config = {
  headers: { 'Content-Type': 'application/json' }
}

export default {
  name: 'PostForm',
  components: {VueChartJS, Table},

  data () {
    return {
      hasTerrass: 0,
      hasBalcony: 0,
      hasSauna: 0,
      hasPool: 0,
      selectedHeating: [],
      energyClass: '',
      houseMaterial: '',
      cityPart: '',
      floor: 0,
      buildYear: 2020,
      houseCondition: 0,
      rooms: 0,
      areaMeters: 0,
      predicted_price: 0
    }
  },
  methods: {
    conditionMapping () {
      if (this.houseCondition === 1) {
        return 'uusehitis'
      } else if (this.houseCondition === 2) {
        return 'renoveeritud'
      } else if (this.houseCondition === 3) {
        return 'remonti vajav'
      } else {
        return ''
      }
    },
    getPredictionFromBackend () {
      if (this.selectedHeating.length === 0) {
        this.selectedHeating.push('keskküte')
      }
      if (this.energyClass.length === 0) {
        this.energyClass = 'a'
      }
      if (this.houseMaterial.length === 0) {
        this.houseMaterial = 'plokkmaja'
      }
      const path = `http://localhost:5000/api/predict`
      axios.post(path, {
        area_meters: Number(this.areaMeters),
        condition: Number(this.houseCondition),
        rooms: Number(this.rooms),
        floor: Number(this.floor),
        build_year: Number(this.buildYear),
        terrass: Number(this.hasTerrass),
        balcony: Number(this.hasBalcony),
        sauna: Number(this.hasSauna),
        pool: Number(this.hasPool),
        linnaosa: this.cityPart,
        house_material: this.houseMaterial,
        heating: this.selectedHeating,
        energy_class: this.energyClass
      }, config)
        .then(response => {
          this.predicted_price = response.data.predicted_price
        })
        .catch(error => {
          console.log(error)
          console.log(error.data)
        })
    }
  }
}
</script>

<style scoped>

</style>
