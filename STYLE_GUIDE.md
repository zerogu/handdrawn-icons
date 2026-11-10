# Hand-drawn illustration style guide

## Design principles

本仓库服务于 AI Skill、Agent、知识库和办公工具市场。插画需要像最初的黑白手绘示例一样饱满、有趣、有质感，而非普通统一描边的 UI 符号。

- 黑白高反差：黑色粗实线、白色内部空间和局部实心黑块。
- 手绘轻拟物：允许轻微不规则，保留前后层叠、透视和笔触的变化。
- 图案必须完整：底部轮廓、手柄、耳罩、书脊等不得裁切。
- 不再添加所有图标统一的「右上角三撇」装饰。
- 不含文字、标注、彩色底板或图片卡片。图标使用透明背景。
- 图形主体四周预留 10%–15% 安全边距，且视觉重心一致。
- 特征明确：Agent 是有黑色面罩和白眼睛的可爱机器人；Translate 是地球和语言气泡；Knowledge 是有厚度的叠书。

## Creation workflow

1. 先从选定的风格原稿出发，**逐枚独立生成或绘制**高分辨率图像，不要将大拼图裁切作为正式制作流程。
2. 将母版保存为 512×512 或更高分辨率的透明 PNG 到 `sources/<style>/vN/`。
3. 检查背景 alpha 与线条边缘；不要以自动阈值抠图损伤白色内部空间。
4. 从母版导出 512×512 lossless WebP 到 `assets/<style>/vN/`。
5. 分别在 32 / 40 / 48 / 64 px 下，对浅蓝、浅紫、浅粉、浅灰背景做真实页面预览。
6. 使用检查脚本验证非透明像素边界不会触及画布边缘。
7. 经视觉验收后更新 `manifest.json`、预览图和 README。

## Acceptance checklist

- [ ] 独立画作而不是从整图硬切的低清图块
- [ ] 主体完整，尤其底部曲线和描边
- [ ] 透明通道正确、无浅灰背景残留或白边
- [ ] 不含统一装饰三撇和英文标签
- [ ] 40px 显示可辨认、线条不会挤成一团
- [ ] 风格与既有图标和谐
- [ ] 原始高清图可追溯，图标 ID 稳定

## Versioning and naming

使用小写 kebab-case，例如 `code`、`agent`、`translate`。不同视觉风格分目录存储，如 `hand-drawn/v1`、`colored-doodle/v1`。已发布版本不要原地覆盖，视觉升级另建 `v2`，避免缓存和业务回归。

## Usage notes

WebP 是位图：背景颜色应在 React 容器上由 CSS 控制；图标内部的笔触颜色不能像 `currentColor` 一样直接重着色。建议业务数据持久化 `style + version + iconId` 而不是完整 CDN URL。

## Licensing

AI 生成素材和代码应分别确认授权策略；在没有正式 LICENSE 前，请勿宣称本仓库是 MIT 或 CC0 授权。
