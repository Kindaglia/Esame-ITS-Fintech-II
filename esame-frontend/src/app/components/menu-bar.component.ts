import { Component } from "@angular/core";
import { MenuItem } from "primeng/api";

@Component({
    selector: 'app-menu-bar',
    templateUrl: './menu-bar.component.html',
    styleUrls: ['./menu-bar.component.scss']
})
export class MenuBarComponent {
    items: MenuItem[] = [];

    ngOnInit() {
        this.items = [
            /* {
                label: 'Home',
                icon: 'pi pi-home',
                routerLink: '/'
            }, */
            {
                label: 'Produttività',
                icon: 'pi pi-user',
                routerLink: '/produttivita'
            },
            {
                label: 'Media percentuale',
                icon: 'pi pi-envelope',
                routerLink: '/media-percentuale'
            },
            {
                label: 'Media Variazione',
                icon: 'pi pi-envelope',
                routerLink: '/media-variazione'
            }
        ];
    }

}

