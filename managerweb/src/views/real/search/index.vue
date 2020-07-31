<template>
  <el-table ref="table" v-loading="tableLoading" :data="tableData" border style="width: 100%" :row-class-name="tableRowClassName">
    <el-table-column align="center" prop="site" label="服务器位置" width="240" />
    <el-table-column align="center" prop="hostname" label="主机名" width="170" />
    <el-table-column align="center" prop="prodip" label="业务网IP" width="120" />
    <el-table-column align="center" prop="dataip" label="数据网IP" width="120" />
    <el-table-column align="center" prop="mgmtip" label="带内网IP" width="120" />
    <el-table-column align="center" prop="outip" label="带外网IP" width="120" />
    <el-table-column align="center" prop="department" label="使用部门" width="140" />
    <el-table-column align="center" prop="status" label="状态" width="120" />
    <el-table-column align="center" prop="use" label="用途" width="200" />
    <el-table-column align="center" label="操作" width="300">
      <template slot-scope="props">
        <el-dropdown style="margin-right: 10px;" @command="handleAddColor">
          <el-button size="mini" type="primary" plain style="background-color: #CBF4B4;">标记</el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item style="background-color: #67C23A" :command="handleAddColorItem('normal', props.$index)">正常</el-dropdown-item>
            <el-dropdown-item style="background-color: #E6A23C" :command="handleAddColorItem('warning', props.$index)">异常</el-dropdown-item>
            <el-dropdown-item style="background-color: #F56C6C" :command="handleAddColorItem('danger', props.$index)">故障</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-button size="mini" type="primary" plain @click="handleCheck(props.$index, props.row)">查看</el-button>
        <el-button size="mini" type="warning" plain @click="handleEdit(props.$index, props.row)">编辑</el-button>
        <el-button size="mini" type="danger" plain @click="handleDelete(props.$index, props.row)">删除</el-button>
      </template>
    </el-table-column>
    <el-table-column type="expand">
      <template slot-scope="props">
        <transition name="el-zoom-in-top">
          <el-form v-show="props.$index === currentRowIndex" label-position="left" inline class="demo-table-expand">
            <el-form-item label="操作系统：">
              <span>{{ props.row.release }}</span>
            </el-form-item>
            <el-form-item label="带外用户名：">
              <span>{{ props.row.outuser }}</span>
            </el-form-item>
            <el-form-item label="带外密码：">
              <span>{{ props.row.outpassword }}</span>
            </el-form-item>
            <el-form-item label="设备类型：">
              <span>{{ props.row.deviceclass }}</span>
            </el-form-item>
            <el-form-item label="设备规格：">
              <span>{{ props.row.format }}</span>
            </el-form-item>
            <el-form-item label="CPU厂商：">
              <span>{{ props.row.cpuenterprise }}</span>
            </el-form-item>
            <el-form-item label="CPU型号：">
              <span>{{ props.row.cpumode }}</span>
            </el-form-item>
            <el-form-item label="内存：">
              <span>{{ props.row.memory }}</span>
            </el-form-item>
            <el-form-item label="硬盘规格：">
              <span>{{ props.row.harddisktype }}</span>
            </el-form-item>
            <el-form-item label="硬盘：">
              <span>{{ props.row.harddisk }}</span>
            </el-form-item>
            <el-form-item label="硬盘备注：">
              <span>{{ props.row.harddiskdes }}</span>
            </el-form-item>
            <el-form-item label="U数：">
              <span>{{ props.row.u }}</span>
            </el-form-item>
            <el-form-item label="资产归属：">
              <span>{{ props.row.owner }}</span>
            </el-form-item>
            <el-form-item label="维保方：">
              <span>{{ props.row.warranty }}</span>
            </el-form-item>
            <el-form-item label="维保起始日期：">
              <span>{{ props.row.warrantystart }}</span>
            </el-form-item>
            <el-form-item label="维保终止日期：">
              <span>{{ props.row.warrantyend }}</span>
            </el-form-item>
            <el-form-item label="备注：">
              <span>{{ props.row.description }}</span>
            </el-form-item>
          </el-form>
        </transition>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios'
// fade/zoom 等
import 'element-ui/lib/theme-chalk/base.css'
export default {
  data() {
    return {
      tableData: [],
      tableLoading: true,
      currentRowIndex: null,
      currentRow: null,
      currentStatus: true,
      colorItemStatus: ''
    }
  },
  mounted() {
    this.tableLoading = true
    axios
      .get('http://localhost:3001/25')
      .then(res => {
        // console.log(res.data)
        this.tableData = res.data
        this.tableLoading = false
      })
      .catch(err => console.log(err))
  },
  methods: {
    // 按钮设置底色
    handleAddColor(command) {
      this.colorItemStatus = command
    },
    handleAddColorItem(status, index) {
      return [status, index]
    },
    tableRowClassName({ row, rowIndex }) {
      // console.log(this.colorItemStatus)
      if (rowIndex === this.colorItemStatus[1]) {
        if (this.colorItemStatus[0] === 'normal') {
          return 'warning-row'
        } else if (this.colorItemStatus[0] === 'warning') {
          return 'success-row'
        } else if (this.colorItemStatus[0] === 'danger') {
          return 'success-row'
        }
      }
    },
    // 查看选项自动开闭合
    handleCheck(index, row) {
      const $table = this.$refs.table
      if (this.currentRow === row) {
        this.currentStatus = !this.currentStatus
        this.currentRow = row
        $table.toggleRowExpansion(this.currentRow, this.currentStatus)
        this.$nextTick(() => {
          this.currentRowIndex = index
        })
      } else if (this.currentRow) {
        // 这时候的 currentRow 是上一次点击的那一行
        if (this.currentStatus) {
          $table.toggleRowExpansion(this.currentRow, false)
        } else {
          this.currentStatus = !this.currentStatus
        }
        this.currentRow = row
        $table.toggleRowExpansion(this.currentRow, this.currentStatus)
        this.$nextTick(() => {
          this.currentRowIndex = index
        })
      } else {
        this.currentRow = row
        $table.toggleRowExpansion(this.currentRow, this.currentStatus)
        this.$nextTick(() => {
          this.currentRowIndex = index
        })
      }
    },
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row) {
      console.log(index, row)
    }
  }
}
</script>

<style lang="scss">
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

  .el-dropdown {
    vertical-align: top;
  }
  .el-dropdown + .el-dropdown {
    margin-left: 15px;
  }
  .el-icon-arrow-down {
    font-size: 10px;
  }

  .el-table__expand-column .cell {
    display: none;
  }

  .el-dropdown-menu {
    padding: 0px;
  }

  .el-dropdown-menu__item{
    border: 1px solid;
    font-size: 12px;
    border-radius: 3px;
    width: 54px;
    height: 26px;
    padding: 7px 15px;
    line-height: 1;
    white-space: nowrap;
    text-align: center;
    transition: .1s;
  }
</style>
