# 颜色使用规范

## 1. 颜色系统

### 1.1 基础色板
- **主色（Primary Color）**: `$color-primary: #BF364F`
  - **使用场景**: 主要按钮、重要标识、重要交互元素
  - **禁用场景**: 不适用于大面积背景或次要元素

- **次级色（Secondary Color）**: `$color-secondary: #6D466B`
  - **使用场景**: 次要按钮、辅助标识
  - **禁用场景**: 不应用于突出显示或重要区域

- **第三色（Thirdary Color）**: `$color-thirdary: #8C4653`
  - **使用场景**: 强调色、辅助背景
  - **禁用场景**: 避免与主色混淆

- **强调色（Accent Color）**: `$color-accent: #D94848`
  - **使用场景**: 错误、警告、提醒、警示性按钮
  - **禁用场景**: 不应用于主要按钮或重要元素

- **浅色（Light Color）**: `$color-light: #F2F2F2`
  - **使用场景**: 背景色、框架颜色、次要区域背景
  - **禁用场景**: 不适用于突出显示的区域

- **深色（Dark Color）**: `$color-dark: #262626`
  - **使用场景**: 文本颜色、深色背景
  - **禁用场景**: 不应用于主要按钮或高亮区域

### 1.2 衍生色生成
- **主色亮色**: `$color-primary-light: color.adjust($color-primary, $lightness: 15%)`
  - **使用场景**: 高亮区域、悬停状态、按钮的悬浮效果

- **主色暗色**: `$color-primary-dark: color.adjust($color-primary, $lightness: -10%)`
  - **使用场景**: 被禁用的按钮、背景色、较深区域

- **主色透明色**: `$color-primary-alpha: color.change($color-primary, $alpha: 0.2)`
  - **使用场景**: 背景图层、透明按钮、渐变效果

- **次级色透明色**: `$color-secondary-alpha: color.change($color-secondary, $alpha: 0.3)`
  - **使用场景**: 透明背景、遮罩效果

### 1.3 功能色
- **成功色**: `$color-success: #28a745`
  - **使用场景**: 成功提示、状态信息
  - **禁用场景**: 不适用于错误或警告信息

- **警告色**: `$color-warning: #ffc107`
  - **使用场景**: 警告提示、待确认的操作按钮
  - **禁用场景**: 不应用于成功或信息提示区域

- **信息色**: `$color-info: #17a2b8`
  - **使用场景**: 信息提示、链接按钮、对话框背景

### 1.4 中性色
- **中性色阶梯**: `$color-neutral`
  - 颜色值：
    - `"0": #FFFFFF` — 白色
    - `"50": #F8F9FA` — 极浅灰
    - `"100": #E9ECEF` — 浅灰
    - `"200": #DEE2E6` — 灰色
    - `"300": #CED4DA` — 中灰
    - `"400": #ADB5BD` — 深灰
    - `"500": #6C757D` — 中性灰
    - `"600": #495057` — 深灰
    - `"700": #343A40` — 极深灰
    - `"800": #212529` — 黑色
    - `"900": #000000` — 黑色
    - `"alice": aliceblue — Alice 蓝色（用于背景）

## 2. 文字色

### 2.1 默认文字色
- **主要文字色**: `$text-colors-primary`
  - **使用场景**: 正文文字、重要说明
  - **禁用场景**: 不应用于背景或低对比度区域

- **次要文字色**: `$text-colors-secondary`
  - **使用场景**: 次要文字、辅助文本
  - **禁用场景**: 不适用于正文或高对比度区域

- **弱化文字色**: `$text-colors-muted`
  - **使用场景**: 不重要或注释性的文字
  - **禁用场景**: 不适用于强调信息

- **浅色文字**: `$text-colors-light`
  - **使用场景**: 浅色背景上的文字，辅助文本
  - **禁用场景**: 不适用于深色背景上的重要文字

## 3. 使用规范

- **对比度**：在使用主色、次级色及其他颜色时，确保与背景色之间有足够的对比度，以保证良好的可读性。
- **一致性**：颜色应当在不同页面、模块中保持一致，避免过多的颜色变化，确保界面风格的统一。
- **辅助色**：尽量避免过多使用辅助色，确保主色调的突出作用。
- **可访问性**：考虑色盲用户，避免依赖颜色区分信息，必要时可以结合文本或图标来传递信息。

## 4. 颜色应用示例

```scss
/* 主按钮 */
button.primary {
  background-color: $color-primary;
  color: $color-light;
}

/* 次级按钮 */
button.secondary {
  background-color: $color-secondary;
  color: $color-light;
}

/* 提示信息 */
.alert-info {
  background-color: $color-info;
  color: $color-light;
}

/* 成功提示 */
.alert-success {
  background-color: $color-success;
  color: $color-light;
}

/* 错误提示 */
.alert-error {
  background-color: $color-accent;
  color: $color-light;
}
