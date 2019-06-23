from bl_ui.properties_world import WorldButtonsPanel
from bpy.types import Panel
from . import bpy
from . import icons

# from ..utils import ui as utils_ui
# from .light import draw_vismap_ui
#
# class LUXCORE_PT_context_world(WorldButtonsPanel, Panel):
#     """
#     World UI Panel
#     """
#     COMPAT_ENGINES = {"LUXCORE"}
#     bl_label = ""
#     bl_options = {"HIDE_HEADER"}
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return context.world and engine == "LUXCORE"
#
#     def draw(self, context):
#         layout = self.layout
#         world = context.world
#         layout.prop(world.luxcore, "light", expand=True)
#
#         if world.luxcore.light != "none":
#             split = layout.split()
#
#             col = split.column(align=True)
#             col.prop(world.luxcore, "rgb_gain", text="")
#
#             is_sky = world.luxcore.light == "sky2"
#             has_sun = world.luxcore.sun and world.luxcore.sun.type == "LAMP"
#
#             if is_sky and has_sun and world.luxcore.use_sun_gain_for_sky:
#                 col.prop(world.luxcore.sun.data.luxcore, "gain")
#             else:
#                 col.prop(world.luxcore, "gain")
#
#             if is_sky and has_sun:
#                 col.prop(world.luxcore, "use_sun_gain_for_sky")
#
#             col = split.column(align=True)
#             op = col.operator("luxcore.switch_space_data_context", text="Show Light Groups")
#             op.target = "SCENE"
#             lightgroups = context.scene.luxcore.lightgroups
#             col.prop_search(world.luxcore, "lightgroup",
#                             lightgroups, "custom",
#                             icon=icons.LIGHTGROUP, text="")
#
#
# class LUXCORE_WORLD_PT_sky2(WorldButtonsPanel, Panel):
#     """
#     Sky2 UI Panel
#     """
#     COMPAT_ENGINES = {"LUXCORE"}
#     bl_label = "Sky Settings"
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return context.world and engine == "LUXCORE" and context.world.luxcore.light == "sky2"
#
#     def draw(self, context):
#         layout = self.layout
#         world = context.world
#
#         layout.prop(world.luxcore, "sun")
#         sun = world.luxcore.sun
#         if sun:
#             is_really_a_sun = sun.type == "LAMP" and sun.data and sun.data.type == "SUN"
#
#             if is_really_a_sun:
#                 layout.label(text="Using turbidity of sun light:", icon=icons.INFO)
#                 layout.prop(sun.data.luxcore, "turbidity")
#             else:
#                 layout.label(text="Not a sun lamp", icon=icons.WARNING)
#         else:
#             layout.prop(world.luxcore, "turbidity")
#
#         # Note: ground albedo can be used without ground color
#         layout.prop(world.luxcore, "groundalbedo")
#         layout.prop(world.luxcore, "ground_enable")
#
#         if world.luxcore.ground_enable:
#             layout.prop(world.luxcore, "ground_color")
#
#
# class LUXCORE_WORLD_PT_infinite(WorldButtonsPanel, Panel):
#     """
#     Infinite UI Panel
#     """
#     COMPAT_ENGINES = {"LUXCORE"}
#     bl_label = "HDRI Settings"
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return context.world and engine == "LUXCORE" and context.world.luxcore.light == "infinite"
#
#     def draw(self, context):
#         layout = self.layout
#         world = context.world
#
#         layout.template_ID(world.luxcore, "image", open="image.open")
#
#         sub = layout.column()
#         sub.enabled = world.luxcore.image is not None
#         sub.prop(world.luxcore, "gamma")
#         world.luxcore.image_user.draw(sub, context.scene)
#         sub.prop(world.luxcore, "rotation")
#         sub.label(text="For free transformation use a hemi lamp", icon=icons.INFO)
#         sub.prop(world.luxcore, "sampleupperhemisphereonly")
#
#
# class LUXCORE_WORLD_PT_volume(WorldButtonsPanel, Panel):
#     """
#     World UI Panel, shows world volume settings
#     """
#     COMPAT_ENGINES = {"LUXCORE"}
#     bl_label = "World Volume"
#     bl_options = {"DEFAULT_CLOSED"}
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return context.world and engine == "LUXCORE"
#
#     def draw(self, context):
#         layout = self.layout
#         world = context.world
#
#         layout.label(text="Default Volume (used on materials without attached volume):")
#         utils_ui.template_node_tree(layout, world.luxcore, "volume", icons.NTREE_VOLUME,
#                                     "LUXCORE_VOLUME_MT_world_select_volume_node_tree",
#                                     "luxcore.world_show_volume_node_tree",
#                                     "luxcore.world_new_volume_node_tree",
#                                     "luxcore.world_unlink_volume_node_tree")
#
#
# class LUXCORE_WORLD_PT_performance(WorldButtonsPanel, Panel):
#     """
#     World UI Panel, shows stuff that affects the performance of the render
#     """
#     COMPAT_ENGINES = {"LUXCORE"}
#     bl_label = "Performance"
#     bl_options = {"DEFAULT_CLOSED"}
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return context.world and engine == "LUXCORE" and context.world.luxcore.light != "none"
#
#     def draw(self, context):
#         layout = self.layout
#         world = context.world
#
#         layout.prop(world.luxcore, "importance")
#         draw_vismap_ui(layout, world)


class LUXCORE_WORLD_PT_visibility(WorldButtonsPanel, Panel):
   COMPAT_ENGINES = {"LUXCORE"}
   bl_label = "Visibility"
   bl_options = {"DEFAULT_CLOSED"}
   @classmethod
   def poll(cls, context):
      engine = context.scene.render.engine
      visible = context.world and context.world.luxcore.light != "none"
      return engine == "LUXCORE" and visible

   def draw(self, context):
      layout = self.layout
      world = context.world

      # These settings only work with PATH and TILEPATH, not with BIDIR
      enabled = context.scene.luxcore.config.engine == "PATH"
      layout.use_property_split = True
      layout.use_property_decorate = False

      col = layout.column(align=True)
      col.enabled = enabled
      col.label(text="Visibility for indirect light rays:")
      col = layout.column(align=True)
      col.prop(world.luxcore, "visibility_indirect_diffuse")
      col.prop(world.luxcore, "visibility_indirect_glossy")
      col.prop(world.luxcore, "visibility_indirect_specular")

      if not enabled:
         layout.label(text="Only supported by Path engines (not by Bidir)", icon=icons.INFO)


def compatible_panels():
   panels = [
      "WORLD_PT_context_world",
      "WORLD_PT_custom_props",
   ]
   types = bpy.types
   return [getattr(types, p) for p in panels if hasattr(types, p)]


def register():
   for panel in compatible_panels():
      panel.COMPAT_ENGINES.add("LUXCORE")  


def unregister():
   for panel in compatible_panels():
      panel.COMPAT_ENGINES.remove("LUXCORE")

