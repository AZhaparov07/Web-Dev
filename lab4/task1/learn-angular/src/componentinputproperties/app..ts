import {Component} from '@angular/core';
import {User} from './componentinputprop';

@Component ({
  selector: 'app-root',
  template: `<app-user name="Simran" /> `,
  imports:[User],
})

export class App {}