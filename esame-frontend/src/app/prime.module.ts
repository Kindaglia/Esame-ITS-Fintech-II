import { NgModule } from '@angular/core';

import { TableModule } from 'primeng/table';
import { MultiSelectModule } from 'primeng/multiselect';
import { DropdownModule } from 'primeng/dropdown';
import { TreeTableModule } from 'primeng/treetable';
import { ToggleButtonModule } from 'primeng/togglebutton';
import { RadioButtonModule } from 'primeng/radiobutton';
import { CheckboxModule } from 'primeng/checkbox';
import { MenuModule } from 'primeng/menu';
import { InputNumberModule } from 'primeng/inputnumber';
import { ListboxModule } from 'primeng/listbox';
import { TooltipModule } from 'primeng/tooltip';
import { ToastModule } from 'primeng/toast';
import { ButtonModule } from 'primeng/button';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { SkeletonModule } from 'primeng/skeleton';
import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { InputTextModule } from 'primeng/inputtext';
import { TabViewModule } from 'primeng/tabview';
import { DialogModule } from 'primeng/dialog';
import { DividerModule } from 'primeng/divider';
import { FieldsetModule } from 'primeng/fieldset';
import { ScrollPanelModule } from 'primeng/scrollpanel';
import { KeyFilterModule } from 'primeng/keyfilter';
import { ProgressBarModule } from 'primeng/progressbar';
import { OverlayPanelModule } from 'primeng/overlaypanel';
import { FileUploadModule } from 'primeng/fileupload';
import { DataViewModule } from 'primeng/dataview';
import { VirtualScrollerModule } from 'primeng/virtualscroller';
import { MenubarModule } from 'primeng/menubar';
import { TreeModule } from 'primeng/tree';
import { CardModule } from 'primeng/card';
import { TagModule } from 'primeng/tag';
import { AccordionModule } from 'primeng/accordion';
import { ChipModule } from 'primeng/chip';

import { BadgeModule } from 'primeng/badge';

const modules = [
    MenubarModule,
    TagModule,
    FileUploadModule,
    ProgressBarModule,
    CheckboxModule,
    TreeTableModule,
    TableModule,
    MultiSelectModule,
    DropdownModule,
    InputNumberModule,
    ToggleButtonModule,
    RadioButtonModule,
    ListboxModule,
    MenuModule,
    ButtonModule,
    InputTextareaModule,
    SkeletonModule,
    ProgressSpinnerModule,
    TooltipModule,
    ToastModule,
    InputTextModule,
    TabViewModule,
    DialogModule,
    DividerModule,
    FieldsetModule,
    ScrollPanelModule,
    KeyFilterModule,
    ProgressBarModule,
    OverlayPanelModule,
    DataViewModule,
    VirtualScrollerModule,
    CardModule,
    TreeModule,
    AccordionModule,
    ChipModule,

    BadgeModule
];

@NgModule({
    imports: modules,
    exports: modules,
    providers: []
})

export class PrimeModule { }
