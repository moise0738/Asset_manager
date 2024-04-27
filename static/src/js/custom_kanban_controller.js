odoo.define('custom_module.CustomKanbanController', function (require) {
    'use strict';

    var KanbanController = require('web.KanbanController');

    var CustomKanbanController = KanbanController.extend({
        _onDragStart: function (ev) {
            var $draggedItem = $(ev.target).closest('.o_kanban_record');
            $draggedItem.addClass('dragging');
        },

        _onDragOver: function (ev) {
            ev.preventDefault();
            $(ev.target).closest('.oe_kanban_column').addClass('droppable');
        },

        _onDrop: function (ev) {
            ev.preventDefault();
            var $draggedItem = $(ev.target).closest('.o_kanban_record');
            var $targetColumn = $(ev.target).closest('.oe_kanban_column');
            $draggedItem.appendTo($targetColumn.find('.o_kanban_content'));
            $targetColumn.removeClass('droppable');
            $draggedItem.removeClass('dragging');
        },

        _onDragEnd: function (ev) {
            $('.oe_kanban_column').removeClass('droppable');
            $('.o_kanban_record').removeClass('dragging');
        },
    });

    return CustomKanbanController;
});
