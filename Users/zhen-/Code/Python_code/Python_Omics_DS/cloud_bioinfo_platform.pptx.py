
# Function to set background image of slide with transparency
def set_background_image(slide, image_path):
    # Add a picture as background
    left = Inches(0)
    top = Inches(0)
    width = Inches(10)
    height = Inches(7)
    pic = slide.shapes.add_picture(image_path, left, top, width, height)
    
    # Set the picture as background with transparency
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)  # White background for overlay
    
    # Make the picture semi-transparent by adjusting its brightness and opacity
    pic.line.color.rgb = RGBColor(255, 255, 255)  # Transparent border
    pic.fill.solid()
    pic.fill.fore_color.rgb = RGBColor(255, 255, 255)  # Transparent fill
    pic.fill.transparency = 0.7  # Adjust transparency level (0 = fully opaque, 1 = fully transparent)

# Slide 3: Introduction (Updated with design from image)
slide_layout = prs.slide_layouts[1]
def add_introduction_slide(prs):
    slide = prs.slides.add_slide(slide_layout)
    
    # 添加背景图片
    set_background_image(slide, "background_image.png")  # 确保图片在同一路径下
    
    # 添加标题
    title_shape = slide.shapes.title
    title_shape.text = "标题内容概述"
    title_shape.text_frame.paragraphs[0].font.size = Pt(32)
    title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(139, 48, 36)
    title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    # 添加编号圆圈 - 根据图片调整位置和大小
    left = Inches(0.8)
    top = Inches(2.0)
    width = Inches(2.0)
    height = Inches(2.0)
    circle = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        left, top, width, height
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = RGBColor(139, 48, 36)
    circle.line.color.rgb = RGBColor(139, 48, 36)
    
    # 添加编号文本
    txBox = circle.text_frame
    p = txBox.paragraphs[0]
    p.text = "03"
    p.font.size = Pt(30)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER
    
    # 添加内容列表
    content_shape = slide.shapes.placeholders[1]
    content_shape.text = (
        "• 标题文字内容\n"
        "• 标题文字内容\n"
        "• 标题文字内容\n"
        "• 标题文字内容"
    )
    content_shape.text_frame.paragraphs[0].font.size = Pt(18)
    content_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(139, 48, 36)
    
    # 定位内容列表到圆圈右侧，根据图片调整位置
    content_shape.left = Inches(3.0)
    content_shape.top = Inches(2.2)
    content_shape.width = Inches(6.0)
    content_shape.height = Inches(2.0)

add_introduction_slide(prs)
