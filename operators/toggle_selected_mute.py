import bpy


class ToggleSelectedMute(bpy.types.Operator):
    bl_idname = 'power_sequencer.toggle_selected_mute'
    bl_label = 'Toggle Selected Mute'
    bl_description = 'Mute or unmute selected sequences'
    bl_options = {'REGISTER', 'UNDO'}

    use_unselected = bpy.props.BoolProperty(
        name="Use unselected",
        description="Toggle non selected sequences",
        default=False)

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        selection = bpy.context.selected_sequences

        if self.use_unselected:
            selection = [
                s for s in bpy.context.sequences if s not in selection
            ]

        if not selection:
            self.report({"WARNING"}, "No sequences to toggle muted")
            return {'CANCELLED'}

        mute = not selection[0].mute
        for s in selection:
            s.mute = mute
        return {'FINISHED'}
