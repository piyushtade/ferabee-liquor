import bpy
import bmesh
import math
import os

def create_ferabee_3d_scene():
    # -------------------------------------------------------------
    # 1. INITIALIZE & CLEAN SCENE
    # -------------------------------------------------------------
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    
    # Configure Render Engine (Eevee / Cycles)
    try:
        scene.render.engine = 'CYCLES'
        scene.cycles.samples = 64
        scene.cycles.use_adaptive_sampling = True
    except:
        scene.render.engine = 'BLENDER_EEVEE_NEXT' if 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'

    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = False

    # -------------------------------------------------------------
    # 2. PBR MATERIAL BUILDERS
    # -------------------------------------------------------------
    def get_or_create_material(name):
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        nodes.clear()
        
        output = nodes.new(type='ShaderNodeOutputMaterial')
        output.location = (400, 0)
        return mat, nodes, links, output

    # 2A. Ultra-Pure Flint Glass Material
    glass_mat, g_nodes, g_links, g_out = get_or_create_material("FeraBee_Flint_Glass")
    bsdf_glass = g_nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf_glass.location = (0, 0)
    bsdf_glass.inputs['Base Color'].default_value = (0.98, 0.98, 1.0, 1.0)
    bsdf_glass.inputs['Roughness'].default_value = 0.02
    bsdf_glass.inputs['IOR'].default_value = 1.52
    if 'Transmission Weight' in bsdf_glass.inputs:
        bsdf_glass.inputs['Transmission Weight'].default_value = 1.0
    elif 'Transmission' in bsdf_glass.inputs:
        bsdf_glass.inputs['Transmission'].default_value = 1.0
    g_links.new(bsdf_glass.outputs['BSDF'], g_out.inputs['Surface'])

    # 2B. Amber Honey Single Malt Liquid Material
    liquid_mat, l_nodes, l_links, l_out = get_or_create_material("FeraBee_Amber_Whisky")
    bsdf_liq = l_nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf_liq.location = (0, 0)
    bsdf_liq.inputs['Base Color'].default_value = (0.95, 0.52, 0.08, 1.0) # Golden Amber
    bsdf_liq.inputs['Roughness'].default_value = 0.01
    bsdf_liq.inputs['IOR'].default_value = 1.33
    if 'Transmission Weight' in bsdf_liq.inputs:
        bsdf_liq.inputs['Transmission Weight'].default_value = 0.92
    elif 'Transmission' in bsdf_liq.inputs:
        bsdf_liq.inputs['Transmission'].default_value = 0.92
    l_links.new(bsdf_liq.outputs['BSDF'], l_out.inputs['Surface'])

    # Volume Absorption for rich amber depth in Cycles
    vol_absorb = l_nodes.new(type='ShaderNodeVolumeAbsorption')
    vol_absorb.location = (0, -200)
    vol_absorb.inputs['Color'].default_value = (0.85, 0.38, 0.04, 1.0)
    vol_absorb.inputs['Density'].default_value = 2.5
    l_links.new(vol_absorb.outputs['Volume'], l_out.inputs['Volume'])

    # 2C. Royal Brushed Gold Metallic Material
    gold_mat, m_nodes, m_links, m_out = get_or_create_material("FeraBee_Royal_Gold")
    bsdf_gold = m_nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf_gold.location = (0, 0)
    bsdf_gold.inputs['Base Color'].default_value = (0.98, 0.82, 0.42, 1.0) # 24K Gold
    bsdf_gold.inputs['Metallic'].default_value = 1.0
    bsdf_gold.inputs['Roughness'].default_value = 0.22
    m_links.new(bsdf_gold.outputs['BSDF'], m_out.inputs['Surface'])

    # 2D. Obsidian Label Material with Gold Accents
    label_mat, lb_nodes, lb_links, lb_out = get_or_create_material("FeraBee_Obsidian_Label")
    bsdf_label = lb_nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf_label.location = (0, 0)
    bsdf_label.inputs['Base Color'].default_value = (0.025, 0.03, 0.04, 1.0) # Deep Obsidian
    bsdf_label.inputs['Roughness'].default_value = 0.35
    lb_links.new(bsdf_label.outputs['BSDF'], lb_out.inputs['Surface'])

    # -------------------------------------------------------------
    # 3. PROCEDURAL 3D MESH MODELING: HEXAGONAL BOTTLE
    # -------------------------------------------------------------
    # Hexagonal Decanter Body
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.95, depth=2.4, location=(0, 0, 1.2))
    bottle_obj = bpy.context.active_object
    bottle_obj.name = "FeraBee_Whisky_Bottle_Glass"
    bottle_obj.data.materials.append(glass_mat)

    # Bevel modifier for luxury faceted glass edges
    bev = bottle_obj.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.08
    bev.segments = 4

    # Shoulder and Neck
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.95, radius2=0.32, depth=0.8, location=(0, 0, 2.8))
    shoulder_obj = bpy.context.active_object
    shoulder_obj.name = "Bottle_Shoulder"
    shoulder_obj.data.materials.append(glass_mat)
    bev_s = shoulder_obj.modifiers.new(name="Bevel", type='BEVEL')
    bev_s.width = 0.06
    bev_s.segments = 3

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.32, depth=1.1, location=(0, 0, 3.75))
    neck_obj = bpy.context.active_object
    neck_obj.name = "Bottle_Neck"
    neck_obj.data.materials.append(glass_mat)

    # Lip Ring
    bpy.ops.mesh.primitive_torus_add(major_radius=0.34, minor_radius=0.06, location=(0, 0, 4.3))
    lip_obj = bpy.context.active_object
    lip_obj.name = "Bottle_Lip"
    lip_obj.data.materials.append(glass_mat)

    # Join Glass Bottle Parts
    bpy.ops.object.select_all(action='DESELECT')
    bottle_obj.select_set(True)
    shoulder_obj.select_set(True)
    neck_obj.select_set(True)
    lip_obj.select_set(True)
    bpy.context.view_layer.objects.active = bottle_obj
    bpy.ops.object.join()
    bpy.ops.object.shade_smooth()

    # Add Subdivision Surface Modifier
    subsurf = bottle_obj.modifiers.new(name="Subdivision", type='SUBSURF')
    subsurf.levels = 1
    subsurf.render_levels = 2

    # -------------------------------------------------------------
    # 4. WHISKY LIQUID MESH (INSIDE CAVITY)
    # -------------------------------------------------------------
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.86, depth=2.2, location=(0, 0, 1.15))
    liquid_body = bpy.context.active_object
    liquid_body.name = "FeraBee_Whisky_Liquid"
    liquid_body.data.materials.append(liquid_mat)
    bev_l = liquid_body.modifiers.new(name="Bevel", type='BEVEL')
    bev_l.width = 0.06
    bev_l.segments = 3

    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.86, radius2=0.26, depth=0.72, location=(0, 0, 2.61))
    liquid_shoulder = bpy.context.active_object
    liquid_shoulder.data.materials.append(liquid_mat)

    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.26, depth=0.5, location=(0, 0, 3.2))
    liquid_neck = bpy.context.active_object
    liquid_neck.data.materials.append(liquid_mat)

    bpy.ops.object.select_all(action='DESELECT')
    liquid_body.select_set(True)
    liquid_shoulder.select_set(True)
    liquid_neck.select_set(True)
    bpy.context.view_layer.objects.active = liquid_body
    bpy.ops.object.join()
    bpy.ops.object.shade_smooth()

    # -------------------------------------------------------------
    # 5. GOLD CLOSURE CAP & CORK STOPPER
    # -------------------------------------------------------------
    # Hexagonal Brushed Gold Cap
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.38, depth=0.75, location=(0, 0, 4.5))
    cap_obj = bpy.context.active_object
    cap_obj.name = "FeraBee_Gold_Cap"
    cap_obj.data.materials.append(gold_mat)
    bev_c = cap_obj.modifiers.new(name="Bevel", type='BEVEL')
    bev_c.width = 0.04
    bev_c.segments = 3
    bpy.ops.object.shade_smooth()

    # Gold Neck Band / Security Seal
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.33, depth=0.3, location=(0, 0, 4.0))
    band_obj = bpy.context.active_object
    band_obj.name = "FeraBee_Neck_Gold_Band"
    band_obj.data.materials.append(gold_mat)
    bpy.ops.object.shade_smooth()

    # -------------------------------------------------------------
    # 6. FRONT OBSIDIAN & GOLD LABEL EMBLEM
    # -------------------------------------------------------------
    bpy.ops.mesh.primitive_plane_add(size=1.2, location=(0, -0.96, 1.3))
    label_obj = bpy.context.active_object
    label_obj.name = "FeraBee_Front_Label"
    label_obj.scale = (0.7, 1.2, 1.0)
    label_obj.rotation_euler = (math.radians(90), 0, 0)
    label_obj.data.materials.append(label_mat)

    # -------------------------------------------------------------
    # 7. LUXURY STUDIO STAGING & 3-POINT LIGHTING
    # -------------------------------------------------------------
    # Studio Curved Backdrop Floor
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
    floor_obj = bpy.context.active_object
    floor_obj.name = "Studio_Backdrop"
    floor_mat, fl_nodes, fl_links, fl_out = get_or_create_material("Studio_Dark_Floor")
    bsdf_fl = fl_nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf_fl.inputs['Base Color'].default_value = (0.015, 0.02, 0.035, 1.0)
    bsdf_fl.inputs['Roughness'].default_value = 0.35
    fl_links.new(bsdf_fl.outputs['BSDF'], fl_out.inputs['Surface'])
    floor_obj.data.materials.append(floor_mat)

    # 7A. Key Strip Light (Left 4000K Warm Gold)
    light_key_data = bpy.data.lights.new(name="Key_Strip_Light", type='AREA')
    light_key_data.energy = 450
    light_key_data.color = (1.0, 0.92, 0.8)
    light_key_data.size = 1.0
    light_key_data.size_y = 5.0
    light_key = bpy.data.objects.new(name="Key_Light", object_data=light_key_data)
    bpy.context.collection.objects.link(light_key)
    light_key.location = (-3.2, -2.8, 3.2)
    light_key.rotation_euler = (math.radians(45), math.radians(-30), math.radians(-45))

    # 7B. Rim/Contour Kicker Light (Right 6500K Cool White Edge Highlight)
    light_rim_data = bpy.data.lights.new(name="Rim_Kicker_Light", type='AREA')
    light_rim_data.energy = 600
    light_rim_data.color = (0.9, 0.95, 1.0)
    light_rim_data.size = 0.6
    light_rim_data.size_y = 6.0
    light_rim = bpy.data.objects.new(name="Rim_Light", object_data=light_rim_data)
    bpy.context.collection.objects.link(light_rim)
    light_rim.location = (3.4, 2.5, 3.5)
    light_rim.rotation_euler = (math.radians(-35), math.radians(45), math.radians(135))

    # 7C. Amber Internal Backlight (Illuminating whisky fluid from behind)
    light_amber_data = bpy.data.lights.new(name="Whisky_Backlight", type='POINT')
    light_amber_data.energy = 180
    light_amber_data.color = (1.0, 0.55, 0.05)
    light_amber_data.shadow_soft_size = 0.5
    light_amber = bpy.data.objects.new(name="Amber_Backlight", object_data=light_amber_data)
    bpy.context.collection.objects.link(light_amber)
    light_amber.location = (0, 1.8, 1.8)

    # 7D. Top Overhead Crown Light
    light_top_data = bpy.data.lights.new(name="Top_Crown_Light", type='AREA')
    light_top_data.energy = 250
    light_top_data.color = (1.0, 0.98, 0.92)
    light_top_data.size = 2.0
    light_top = bpy.data.objects.new(name="Top_Light", object_data=light_top_data)
    bpy.context.collection.objects.link(light_top)
    light_top.location = (0, 0, 7.5)
    light_top.rotation_euler = (0, 0, 0)

    # -------------------------------------------------------------
    # 8. CINEMATIC 85MM CAMERA
    # -------------------------------------------------------------
    cam_data = bpy.data.cameras.new(name="Cinematic_Camera")
    cam_data.lens = 85 # 85mm Portrait Glass
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = bottle_obj
    cam_data.dof.aperture_fstop = 2.8

    cam_obj = bpy.data.objects.new(name="Camera", object_data=cam_data)
    bpy.context.collection.objects.link(cam_obj)
    scene.camera = cam_obj
    cam_obj.location = (0, -6.2, 2.5)
    cam_obj.rotation_euler = (math.radians(78), 0, 0)

    # -------------------------------------------------------------
    # 9. EXPORTS & RENDERS
    # -------------------------------------------------------------
    output_dir = r"C:\Users\piyus\Downloads\ferabee"
    
    # 9A. Save .blend scene file
    blend_path = os.path.join(output_dir, "ferabee_reserve_whisky_3d.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    print(f"Saved Blender Project to: {blend_path}")

    # 9B. Export GLTF/GLB for WebGL / Three.js
    glb_path = os.path.join(output_dir, "ferabee_whisky_bottle.glb")
    bpy.ops.export_scene.gltf(
        filepath=glb_path,
        export_format='GLB',
        use_selection=False,
        export_materials='EXPORT',
        export_cameras=False,
        export_lights=False
    )
    print(f"Exported WebGL 3D Asset to: {glb_path}")

    # 9C. Export Wavefront OBJ
    obj_path = os.path.join(output_dir, "ferabee_whisky_bottle.obj")
    try:
        bpy.ops.wm.obj_export(filepath=obj_path)
    except:
        bpy.ops.export_scene.obj(filepath=obj_path)
    print(f"Exported Universal 3D Model to: {obj_path}")

    # 9D. Render High-Resolution Studio Visual Showcase
    render_path = os.path.join(output_dir, "assets", "blender_render_showcase.png")
    scene.render.filepath = render_path
    bpy.ops.render.render(write_still=True)
    print(f"Rendered Studio 3D Visual to: {render_path}")

if __name__ == "__main__":
    create_ferabee_3d_scene()
