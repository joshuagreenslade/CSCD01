import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { MembersService } from '../../services/members.service';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-member',
  templateUrl: './member.component.html',
  styleUrls: ['./member.component.css']
})
export class MemberComponent implements OnInit {
  
  id:string;
  member: {};

  constructor(private route: ActivatedRoute, private __memberService:MembersService) {}

  ngOnInit() {
    this.route.params
          .map(params => params['id'])
          .subscribe((id) => {
            this.__memberService
              .getMembers()
              .subscribe(members => {
                  this.member = members.members[id]}
              );
          });
  }

}
